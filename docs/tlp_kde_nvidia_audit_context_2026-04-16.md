# Audit Context: TLP + KDE Plasma + NVIDIA (CachyOS) — 2026-04-16

This document is the **single source of truth** context for the LLM Council audit.  
Goal: evaluate whether the current setup is best-practice for **battery longevity on BAT** and **gaming responsiveness on AC**, on an **Acer Nitro AN515-58** running **CachyOS (Arch-like)** with **KDE Plasma 6.6 (Wayland)** and **NVIDIA RTX 4050 Mobile**.

## 1) System snapshot (evidence)

- **Host**: Acer Nitro AN515-58 (BIOS V2.19, EC 2.12)
- **OS**: CachyOS (Arch-like rolling)
- **Kernel**: `6.19.12-1-cachyos-bore`
- **Init**: systemd 260
- **DE/WM**: KDE Plasma 6.6.4 / KWin (Wayland)
- **GPU**:
  - iGPU: Intel Alder Lake-P (driver `i915`)
  - dGPU: NVIDIA AD107M RTX 4050 Mobile (driver `nvidia`, version 595.58.03)

Relevant command outputs collected during the session:
- `systemctl --user status plasma-powerdevil`: **active (running)**
- `systemctl status power-profiles-daemon`: initially active; later **masked + inactive**
- `systemctl status tlp`: **enabled**, last run success

## 2) User intent / target behavior

- **On battery (BAT)**: “smooth + longer” (battery drains slower, still responsive)
- **On AC (charger)**: “gaming + maximum responsiveness/performance”

## 3) Actions performed (what changed)

### 3.1. Resolve conflicts: TLP vs power-profiles-daemon (PPD)

Reason: TLP and PPD both manage overlapping tunables; running both is not recommended.

Actions:
- `power-profiles-daemon` was stopped and **masked** (confirmed later by systemctl).
- TLP was installed and enabled:
  - Packages: `tlp`, `tlp-rdw`
  - Service: `tlp.service` enabled; successful init run.

### 3.2. Add custom TLP policy for this laptop

We created a custom override file:

- Path: `/etc/tlp.d/99-adsnitro.conf`

Intent:
- **AC**: performance profile (CPU governor, EPP, platform_profile; avoid latency-saving toggles that hurt gaming)
- **BAT**: balanced / balance_power (keep smoothness, reduce wasted power)

Key settings written:
- CPU scaling governor:
  - AC: `performance`
  - BAT: `powersave`
- CPU energy/performance policy (EPP):
  - AC: `performance`
  - BAT: `balance_power`
- CPU boost:
  - AC: enabled
  - BAT: enabled (for responsiveness; may reduce battery life)
- HWP dynamic boost:
  - AC: enabled
  - BAT: disabled
- ACPI platform profile:
  - AC: `performance`
  - BAT: `balanced`
- Wi-Fi power save:
  - AC: off
  - BAT: (left default TLP behavior)
- Sound power save:
  - AC: off

### 3.3. PCIe power saving on battery

Added to `/etc/tlp.d/99-adsnitro.conf`:
- `PCIE_ASPM_ON_AC="default"`
- `PCIE_ASPM_ON_BAT="powersave"`

Applied via:
- `sudo tlp start` (confirmed “TLP started using profile balanced/BAT (auto)” during the session)

### 3.4. USB autosuspend: prevent BT lag/dropouts

Evidence:
- BT device present: Intel AX201 Bluetooth `8087:0026 (btusb)`, connected.
- USB autosuspend was enabled.

Change:
- Added:
  - `USB_EXCLUDE_BTUSB="1"`

Verified via `tlp-stat -u`:
- `Exclude bluetooth = enabled`

### 3.5. NVIDIA runtime power management parameter (pending reboot)

Created:
- `/etc/modprobe.d/nvidia-runtimepm.conf`
  - `options nvidia NVreg_DynamicPowerManagement=0x02`

Note: This change generally requires **reboot** for a clean effect.

## 4) Evidence collected: current power / runtime states

### 4.1. TLP status

- `tlp.service`: success; applies power save settings.
- Current profile shown by TLP during session:
  - `Power profile = balanced/BAT`
  - `Power source = battery`

### 4.2. CPU and platform profile (BAT at time of capture)

From `tlp-stat -p`:
- `scaling_driver = intel_pstate`
- `scaling_governor = powersave`
- `energy_performance_preference (EPP) = balance_power`
- `platform_profile = balanced`

### 4.3. dGPU runtime power vs NVML readings

**Sysfs runtime PM indicates the NVIDIA GPU is suspended**:
- `/sys/bus/pci/devices/0000:01:00.0/power/control = auto`
- `/sys/bus/pci/devices/0000:01:00.0/power/runtime_status = suspended`
- `/sys/bus/pci/devices/0000:01:00.0/power/runtime_suspended_time` increases (example captured: `460941`)

However, **`nvidia-smi` showed ~14W and ~12% util with no running processes**:
- `Pwr:Usage/Cap 14W / 30W`
- `GPU-Util 12%`
- Processes: “No running processes found”

Interpretation hypothesis to evaluate:
- NVML / `nvidia-smi` may briefly **wake** the GPU or report non-representative values during runtime suspend, while sysfs indicates real runtime suspend state.

### 4.4. NVIDIA services

All inactive/disabled/masked:
- `nvidia-powerd`: masked/inactive
- `nvidia-persistenced`: inactive
- `nvidia-suspend/resume/hibernate`: inactive

### 4.5. Attempted diagnostic: unload `nvidia_uvm`

- `sudo modprobe -r nvidia_uvm` did **not** change `/proc/driver/nvidia/.../power` “Video Memory: Active”.

## 5) Known constraints / non-goals

- Battery charge thresholds are **not supported** by this hardware/kernel interface:
  - `charge_control_*_threshold = (not available)`
- We did **not** perform risky module reloads under Wayland; prefer reboot for kernel module parameter changes.

## 6) Questions for the Council (what to evaluate)

1. Is masking `power-profiles-daemon` and using TLP on KDE Plasma 6.6 the best-practice approach for this target behavior?
2. Are the chosen TLP settings safe for gaming responsiveness on AC and stable suspend/resume on Wayland + NVIDIA?
3. Is `PCIE_ASPM_ON_BAT="powersave"` a good default on this platform, or should it remain `default` to avoid device quirks?
4. Should `CPU_BOOST_ON_BAT` remain enabled for “smooth + long”, or be disabled and replaced with other tuning?
5. For NVIDIA dGPU idle power: is `NVreg_DynamicPowerManagement=0x02` appropriate with driver 595.x and this laptop? Any better/safer approach (PRIME offload config, `nvidia-powerd` policy, persistence daemon)?
6. How should we reconcile sysfs “suspended” with `nvidia-smi` showing 14W/12%? What is the correct measurement method to trust?
7. Any additional recommended checks (e.g., `powertop`, `intel_gpu_top`, `cat /proc/driver/nvidia/.../power` timing) and rollback steps?

## 7) Rollback plan (high-level)

- Re-enable PPD:
  - `sudo systemctl unmask power-profiles-daemon && sudo systemctl enable --now power-profiles-daemon`
  - disable TLP: `sudo systemctl disable --now tlp`
- Remove custom TLP overrides:
  - remove `/etc/tlp.d/99-adsnitro.conf`
- Remove NVIDIA module parameter file:
  - remove `/etc/modprobe.d/nvidia-runtimepm.conf`


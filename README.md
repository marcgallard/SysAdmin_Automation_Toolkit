# SysAdmin & Network Automation Toolkit
![OS](https://img.shields.io/badge/OS-Windows%2011-blue) ![Python](https://img.shields.io/badge/Python-3.x-yellow)
## A collection of Python and Bash scripts, automation tools, and registry additions designed to streamline IT operations, network troubleshooting, and endpoint security.

> [!WARNING]
> **REGISTRY MODIFICATION NOTICE**
> Some tools in this repository (specifically the Context Firewall) make direct changes to the Windows Registry. While these scripts have been tested thoroughly on **Windows 11**, always back up your registry before running them. Use at your own risk.

### 📋 Overview
This repository serves as a centralized toolkit for System Administration and Network Operations Center (NOC) tasks. It focuses on automating repetitive CLI workflows, enhancing Windows OS functionality, and performing network diagnostics.

**Core Focus Areas:**
* **Endpoint Security:** Automating firewall rules and access control.
* **Network Operations:** Subnet calculation and availability monitoring.
* **System Integrity:** Registry manipulation and context menu integration.

---

### 📂 Repository Structure

| Category | Tool Name | Description | Stack |
| :--- | :--- | :--- | :--- |
| **Security** | `Context-Firewall-Block` | **[Highlight]** Adds "Block/Allow Network" options directly to the Windows right-click context menu for `.exe` files. | Python, Registry |
| **Network** | `Subnet-Calc-CLI` | *In Progress.* A CLI tool for calculating network IDs, broadcast addresses, and usable host ranges (CIDR). | Python |
| **Monitor** | `Clinical-Uptime` | *Planned.* A latency and packet-loss monitor designed for high-availability healthcare environments. | Python |
| **Utils** | `Log-Rotator` | Simple utility for archiving and clearing local log files. | Bash/Python |

---

### ⭐ Featured Tool: Windows Firewall Context Integration
*(Located in `/endpoint_security/firewall_context/`)*

This project integrates Python with the Windows Registry (`regedit`) to streamline application blocking.
* **Problem:** Blocking an application via `wf.msc` takes ~15 clicks and 45 seconds.
* **Solution:** This tool adds a context menu item to block/allow traffic in 2 seconds.
* **Key Tech:** Uses `ctypes` for privilege escalation and `subprocess` to drive `netsh` commands.

---

### 🛠️ Dependencies & Setup
Most tools in this repository require **Python 3.x**.

**Installation:**
```bash
git clone [https://github.com/YourUsername/sysadmin-toolkit](https://github.com/YourUsername/sysadmin-toolkit)
pip install -r requirements.txt

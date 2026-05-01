import datetime

# Control effectiveness reduction factors
CONTROL_FACTORS = {
    "Strong": 0.3,
    "Moderate": 0.6,
    "Weak": 0.8,
    "None": 1.0
}

def calc_inherent_score(likelihood, impact):
    return likelihood * impact

def calc_inherent_rating(score):
    if score >= 15:
        return "High"
    elif score >= 8:
        return "Medium"
    else:
        return "Low"

def calc_residual_score(inherent, control):
    factor = CONTROL_FACTORS.get(control, 1.0)
    return round(inherent * factor, 1)

def calc_residual_rating(score):
    if score >= 15:
        return "High"
    elif score >= 8:
        return "Medium"
    else:
        return "Low"

RISKS = [
    {
        "risk_id": "RSK-001",
        "category": "Access Control",
        "title": "Unauthorized Privileged Access",
        "description": "Privileged accounts granted excessive access without proper authorization, enabling unauthorized changes or data exfiltration.",
        "likelihood": 4,
        "impact": 5,
        "control_effectiveness": "Moderate",
        "current_controls": "RBAC implemented; Quarterly privileged access reviews; SoD policy",
        "risk_owner": "CISO",
        "department": "IT Security",
        "remediation_action": "Complete overdue Q3 access review; implement automated quarterly certification in IAM tool by Q4 2025",
        "remediation_deadline": "2025-09-30",
        "remediation_status": "In Progress",
        "date_identified": "2025-01-15",
        "last_reviewed": "2025-06-20"
    },
    {
        "risk_id": "RSK-002",
        "category": "Authentication",
        "title": "MFA Bypass / Weak Authentication",
        "description": "Accounts without MFA enforced are vulnerable to phishing and password spraying attacks.",
        "likelihood": 3,
        "impact": 5,
        "control_effectiveness": "Moderate",
        "current_controls": "Azure AD MFA enforcement; Conditional Access policies; Security awareness training",
        "risk_owner": "IT Security Manager",
        "department": "IT Security",
        "remediation_action": "Enroll all non-MFA accounts within 30 days; create exception register with CISO approval; monthly status reporting",
        "remediation_deadline": "2025-07-31",
        "remediation_status": "In Progress",
        "date_identified": "2025-02-01",
        "last_reviewed": "2025-06-25"
    },
    {
        "risk_id": "RSK-003",
        "category": "Segregation of Duties",
        "title": "SoD Conflict in Finance ERP",
        "description": "Single user can create and approve purchase orders in ERP, enabling fictitious vendor payment fraud.",
        "likelihood": 3,
        "impact": 4,
        "control_effectiveness": "Weak",
        "current_controls": "Manual supervisory review of high-value transactions; Internal audit sampling",
        "risk_owner": "Finance Controller",
        "department": "Finance",
        "remediation_action": "Implement ERP role matrix with SoD controls; configure SAP GRC automated SoD detection by Q3 2025",
        "remediation_deadline": "2025-09-15",
        "remediation_status": "Open",
        "date_identified": "2025-03-10",
        "last_reviewed": "2025-06-01"
    },
    {
        "risk_id": "RSK-004",
        "category": "Data Loss Prevention",
        "title": "Sensitive Data Exfiltration via Removable Media",
        "description": "Employees may transfer sensitive data to USB or personal cloud, risking data breach and regulatory non-compliance.",
        "likelihood": 2,
        "impact": 5,
        "control_effectiveness": "Moderate",
        "current_controls": "USB restrictions via Group Policy; DLP monitoring alerts; Acceptable Use Policy",
        "risk_owner": "IT Security Manager",
        "department": "IT Security",
        "remediation_action": "Enable DLP policy enforcement (block mode); conduct DLP effectiveness review; update AUP training",
        "remediation_deadline": "2025-08-30",
        "remediation_status": "In Progress",
        "date_identified": "2025-01-20",
        "last_reviewed": "2025-05-30"
    },
    {
        "risk_id": "RSK-005",
        "category": "Patch Management",
        "title": "Unpatched Critical Vulnerabilities",
        "description": "Systems not patched within SLA exposed to known exploits increasing likelihood of successful cyberattack.",
        "likelihood": 3,
        "impact": 4,
        "control_effectiveness": "Moderate",
        "current_controls": "Monthly patch cycle; Vulnerability scanner (Nessus); Critical patch SLA: 30 days",
        "risk_owner": "IT Operations Lead",
        "department": "IT Operations",
        "remediation_action": "Maintain monthly patch cycle; review 14 overdue patches; escalate unpatched critical CVEs to CISO",
        "remediation_deadline": "2025-07-15",
        "remediation_status": "Open",
        "date_identified": "2025-04-05",
        "last_reviewed": "2025-06-15"
    },
    {
        "risk_id": "RSK-006",
        "category": "Third-Party Risk",
        "title": "Uncontrolled Vendor Access",
        "description": "Third-party vendors with system access may lack appropriate controls, monitoring, or termination procedures.",
        "likelihood": 3,
        "impact": 4,
        "control_effectiveness": "Weak",
        "current_controls": "Vendor access agreements; Vendor register; Annual vendor risk assessment",
        "risk_owner": "Procurement",
        "department": "Procurement",
        "remediation_action": "Implement just-in-time vendor access; enforce MFA for all vendor accounts; complete vendor risk assessments",
        "remediation_deadline": "2025-10-01",
        "remediation_status": "Open",
        "date_identified": "2025-02-15",
        "last_reviewed": "2025-05-20"
    },
    {
        "risk_id": "RSK-007",
        "category": "Incident Response",
        "title": "Inadequate Breach Detection & Response",
        "description": "Insufficient SIEM coverage or slow IR may result in extended dwell time and delayed breach notification.",
        "likelihood": 2,
        "impact": 5,
        "control_effectiveness": "Moderate",
        "current_controls": "SIEM monitoring; Incident response plan; SOC team (business hours only)",
        "risk_owner": "CISO",
        "department": "IT Security",
        "remediation_action": "Extend SOC to 24/7; conduct IR tabletop exercise; update IRP for ransomware scenarios",
        "remediation_deadline": "2025-12-31",
        "remediation_status": "In Progress",
        "date_identified": "2025-01-10",
        "last_reviewed": "2025-06-28"
    },
    {
        "risk_id": "RSK-008",
        "category": "Compliance",
        "title": "GDPR Data Privacy Non-Compliance",
        "description": "Failure to maintain data processing records, consent management, or breach notification risks regulatory fines.",
        "likelihood": 2,
        "impact": 5,
        "control_effectiveness": "Moderate",
        "current_controls": "Privacy policy; Data processing register; DPO appointed; Breach notification procedure",
        "risk_owner": "Data Protection Officer",
        "department": "Legal & Compliance",
        "remediation_action": "Complete data processing register audit; update privacy notices; conduct DPIA for new AI tools",
        "remediation_deadline": "2025-09-30",
        "remediation_status": "In Progress",
        "date_identified": "2025-03-01",
        "last_reviewed": "2025-06-10"
    },
    {
        "risk_id": "RSK-009",
        "category": "Business Continuity",
        "title": "Inadequate DR / RTO Capability",
        "description": "Untested disaster recovery may result in downtime exceeding RTO targets during system failure or ransomware.",
        "likelihood": 2,
        "impact": 4,
        "control_effectiveness": "Moderate",
        "current_controls": "DR plan documented; Annual DR test; Offsite backups; RTO: 4 hours",
        "risk_owner": "IT Operations Lead",
        "department": "IT Operations",
        "remediation_action": "Conduct full DR simulation; validate backup restoration time; test failover to DR site",
        "remediation_deadline": "2025-11-30",
        "remediation_status": "Open",
        "date_identified": "2025-02-20",
        "last_reviewed": "2025-05-15"
    },
    {
        "risk_id": "RSK-010",
        "category": "Physical Security",
        "title": "Unauthorized Physical Access to Server Room",
        "description": "Inadequate physical access controls to server infrastructure could allow hardware theft or sabotage.",
        "likelihood": 1,
        "impact": 4,
        "control_effectiveness": "Strong",
        "current_controls": "Badge access control; CCTV monitoring; Visitor log; Clean desk policy",
        "risk_owner": "Facilities Manager",
        "department": "Facilities",
        "remediation_action": "Monthly badge access log review; CCTV coverage verified; Physical security walkthrough complete",
        "remediation_deadline": "2025-03-01",
        "remediation_status": "Closed",
        "date_identified": "2024-11-01",
        "last_reviewed": "2025-06-01"
    },
    {
        "risk_id": "RSK-011",
        "category": "Insider Threat",
        "title": "Malicious Insider Data Theft",
        "description": "Disgruntled or malicious employee could steal sensitive data using legitimate access credentials.",
        "likelihood": 2,
        "impact": 5,
        "control_effectiveness": "Weak",
        "current_controls": "User behaviour analytics (basic); Exit interviews; Background checks on hire",
        "risk_owner": "CISO",
        "department": "IT Security",
        "remediation_action": "Implement UEBA solution; enhance DLP monitoring; define insider threat response playbook",
        "remediation_deadline": "2026-03-31",
        "remediation_status": "Open",
        "date_identified": "2025-04-20",
        "last_reviewed": "2025-06-20"
    },
    {
        "risk_id": "RSK-012",
        "category": "Cloud Security",
        "title": "Misconfigured Cloud Storage Exposing Data",
        "description": "S3 buckets or Azure Blob storage misconfigured as public could expose sensitive company or customer data.",
        "likelihood": 3,
        "impact": 5,
        "control_effectiveness": "Moderate",
        "current_controls": "Cloud security posture management (CSPM) tool; IaC security scanning; Monthly cloud audit",
        "risk_owner": "Cloud Architect",
        "department": "IT Operations",
        "remediation_action": "Enforce no-public-access policy via org-level policy; remediate 3 identified misconfigurations; automate CSPM alerts",
        "remediation_deadline": "2025-08-01",
        "remediation_status": "In Progress",
        "date_identified": "2025-05-01",
        "last_reviewed": "2025-06-25"
    }
]

# Add calculated fields for each risk
def get_risks_with_scores():
    risks = []
    for r in RISKS:
        inherent = calc_inherent_score(r["likelihood"], r["impact"])
        inherent_rating = calc_inherent_rating(inherent)
        residual = calc_residual_score(inherent, r["control_effectiveness"])
        residual_rating = calc_residual_rating(residual)
        risk = dict(r)
        risk["inherent_score"] = inherent
        risk["inherent_rating"] = inherent_rating
        risk["residual_score"] = residual
        risk["residual_rating"] = residual_rating
        risks.append(risk)
    return risks

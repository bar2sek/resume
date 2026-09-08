# Ryan Bartusek
### Enterprise Cloud Architecture | Cloud Platform Engineering
Des Moines, IA | [bar2sek@users.noreply.github.com](mailto:bar2sek@users.noreply.github.com) | [linkedin.com/in/bar2sek](https://linkedin.com/in/bar2sek)

---
## Professional Summary
Cloud Infrastructure Leader and Enterprise Cloud Architect with 10+ years of experience driving cloud platform maturity across public-sector, financial, and enterprise domains. Proven track record leading engineering teams of 6–10, architecting enterprise multi-account AWS environments across production and non-production, and operationalizing statewide Terraform mandates through engineer enablement and automated change-control governance.

Specializes in aligning strategic business goals with scalable cloud foundations, automated account vending pipelines, and Infrastructure as Code (IaC) delivery models. Demonstrated success establishing architectural standards, multi-environment security guardrails, and modern DevSecOps practices that accelerate developer velocity while maintaining strict compliance and operational resilience. Trusted advisor to executive leadership, security teams, and delivery partners for translating organizational vision into scalable, secure, and sustainable cloud platforms.

---
## Core Competencies
- **Cloud & Platforms:** AWS (Organizations, Control Tower, SCPs, IAM Identity Center, Bedrock, Connect, Transit Gateway, Security Hub, GuardDuty, KMS, Config, CloudTrail), Microsoft Azure (AVD, Entra ID, Azure Policy, Defender for Cloud, Key Vault, Azure Firewall, Management Groups, Log Analytics), VMware Tanzu (TAS, BOSH, BBR, vSphere)
- **Infrastructure as Code & Automation:** Terraform (Enterprise Deployment, Modules, & Standards), AWS CDK (Python), Azure Bicep & ARM Templates, PowerShell (Pester TDD), Bash, GitOps
- **CI/CD & DevSecOps:** GitHub & GitHub Actions (Org Administrator), Azure DevOps, Concourse CI, Docker
- **Networking & Security:** Aviatrix Transit Networking & Distributed Firewalls, SAML / SSO Identity Federation (Okta, Entra ID, Active Directory), Role-Based Access Control (RBAC)
- **Observability & Operations:** Prometheus, Grafana, Azure Monitor, Log Analytics, Nerdio Manager, Selenium
- **Diagramming & Design:** Lucidchart, Miro, Microsoft Visio

---
## Experience

### State of Iowa – Department of Management
**Cloud Infrastructure Team Lead** | *April 2025 – Present*
- **Enterprise AWS OU & Multi-Account Strategy:** Designed and executed a comprehensive multi-tier Organizational Unit (OU) hierarchy across dozens of state agencies; established strict blast-radius isolation between production, non-production, core infrastructure, and agency workloads while enforcing hierarchical Service Control Policies (SCPs), baseline guardrails, and compliance auditing at the OU level.
- **Automated Account Vending (AFT):** Deployed **AWS Account Factory for Terraform (AFT)** and Control Tower, orchestrating GitOps-driven account vending pipelines via GitHub Actions and AWS CodePipeline to automate account provisioning with standardized security baselines, IAM Identity Center, VPC networking, and OU policy inheritance.
- **IaC Tooling Strategy & Standardization:** Conducted technical trade-off evaluations (e.g., **Terraform vs. Azure Bicep & CloudFormation**), establishing Terraform as the enterprise standard; authored reusable module libraries under strict change-control workflows.
- **FinOps & Cost Governance:** Evaluated **Apptio Cloudability** and AWS Cost Management tools to establish enterprise tagging governance, cost attribution, and multi-agency budget visibility.
- **Large-Scale Cloud Migration Support:** Led the infrastructure engineering team collaborating with AWS Professional Services on statewide migration initiatives, utilizing AWS Migration Factory to rehost **1,400+ VMware virtual machines** and core legacy applications for state agencies.
- **GenAI & Emerging Tech Governance:** Partnered with executive leadership, security, and compliance teams to establish the architecture and governance framework for **Amazon Bedrock**, enabling secure generative AI adoption across state operations.
- **Contact Center Modernization:** Led infrastructure delivery and multi-agency greenfield deployment of **Amazon Connect** in collaboration with AWS Professional Services and ScaleCapacity, replacing legacy telephony across four state agencies.
- **Engineering Leadership & Governance:** Managed and coordinated a team of **6–10 cloud engineers and technicians**; instituted structured agile ceremonies, elevated team delivery velocity, and served as GitHub Administrator for change control.
- **Multicloud Networking & Security Strategy:** Spearheaded technical strategy and executive buy-in for **Aviatrix** multicloud transit networking and distributed firewalls, delivering centralized visibility, hybrid connectivity, and advanced security segmentation.

### State of Iowa – Department of Health and Human Services
**Lead Platform Engineer** | *April 2021 – April 2025*
- **Azure Platform & Landing Zones:** Spearheaded architectural design, governance, and deployment of enterprise Azure landing zones in strict alignment with the Microsoft Cloud Adoption Framework (CAF).
- **Virtual Desktop Infrastructure (AVD):** Designed, deployed, and managed Azure Virtual Desktop (AVD) environments utilizing native Azure services and the Nerdio management platform to optimize secure remote access for statewide personnel.
- **Identity Federation & Single Sign-On (SSO):** Engineered enterprise identity federation and SSO workflows, integrating Okta, Microsoft Entra ID (Azure AD), SAML authentication, and on-premises Active Directory.
- **Multicloud Networking POC:** Led proof-of-concept (POC) evaluations for Aviatrix multicloud transit networking to enhance network visibility, security segmentation, and hybrid cloud connectivity.
- **PaaS Platform Engineering:** Orchestrated greenfield configuration and deployment of VMware Tanzu Application Service (TAS) via BOSH on legacy on-premises vSphere infrastructure, partnering with VMware consultants to host refactored state assistance applications (e.g., Rent Reimbursement).
- **CI/CD Automation & Mentorship:** Built CI/CD pipelines utilizing Concourse CI, Platform Automation, and GitOps workflows under strict pull-request controls; drove team growth through technical screening, onboarding, and structured mentorship.

### Principal Financial Group
**Platform Engineer & Developer Support** | *July 2019 – April 2021*
- **AWS IaC & CI/CD Automation:** Supported platform workloads in AWS utilizing AWS CDK (Python) to develop and deploy reusable CloudFormation stacks, establishing automated GitHub Actions CI/CD infrastructure pipelines.
- **Microservices & API Gateway:** Engineered Python and Docker-based platform microservices to extend Tanzu capabilities, including a highly available API gateway bridging cloud-native applications with legacy on-premises SOAP identity services.
- **Pipeline Governance:** Automated CI/CD pipeline governance in Concourse CI, developing custom automation to enforce semantic versioning and Git tagging based on commit keywords for container images.
- **Synthetic Monitoring & Observability:** Built containerized synthetic testing observability tooling using Python and Selenium to monitor authentication paths; created real-time operational health dashboards in Grafana and Prometheus with xMatters alerting integration.
- **Platform Operations & Disaster Recovery:** Managed infrastructure lifecycles via BOSH on VMware vSphere IaaS with Ubuntu VMs; scripted automated disaster recovery using BOSH Backup and Restore (BBR) targeting on-premises MinIO S3 storage buckets over NFS.
- **Developer Enablement:** Authored architectural guides, markdown documentation, and deployment runbooks within Atlassian Confluence to accelerate engineering team onboarding.

### Corteva Agriscience
**Cloud Engineer & Developer Support** | *October 2017 – July 2019*
- **Automation & Test-Driven Development:** Engineered automation scripts using PowerShell and Pester unit testing for Azure Automation Runbooks, streamlining mass virtual machine backups, automated patching schedules, and systems management.
- **Enterprise Workload Optimization:** Supported enterprise workloads in Azure, optimizing virtual machine performance for mission-critical SAP, HANA, Oracle, and SQL deployments running on Red Hat Enterprise Linux (RHEL) and Windows Server.
- **Monitoring & Alerting Frameworks:** Implemented infrastructure monitoring and alerting frameworks using Azure Monitor, Log Analytics, and Azure Alerts to proactively detect and remediate backup and system failures.
- **Engineering Best Practices:** Authored standard operating procedures, technical runbooks, and deployment guides in a centralized repository to establish consistent engineering best practices across vendors and internal teams.
- **Offshore Team Enablement:** Onboarded and trained offshore engineering teams (including Accenture and TCS), serving as the primary technical escalation point for enterprise cloud operations.

---
## Earlier Experience
- **Lean TECHniques** | Software Developer (*October 2016 – May 2017*)
- **EMC Insurance** | Software Developer (*May 2016 – October 2016*)
- **LightEdge Solutions** | Data Center Technician (*January 2014 – May 2016*)
- **IdentoGO by MorphoTrust USA** | Remote & On-Site Support Technician (*August 2011 – December 2013*)

---
## Education
- **Iowa State University** – Bachelor of Arts (BA), Visual Studies
- **Des Moines Area Community College** – Associate of Science (AS), Business Information Systems

---
## Certifications
- **Aviatrix Certified Engineer (ACE)** – Multicloud Network Professional
- **Aviatrix Certified Engineer (ACE)** – Multicloud Network Associate
- **Microsoft Certified:** Azure Fundamentals (AZ-900)
- **Microsoft Certified:** Azure Data Fundamentals (DP-900)
- **AWS Certified Solutions Architect – Associate (SAA-C03)** *(Expected 2026)*

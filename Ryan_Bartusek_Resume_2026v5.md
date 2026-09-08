# Ryan Bartusek

### Enterprise Cloud Architecture | Cloud Platform Engineering

Des Moines, IA | [bar2sek@users.noreply.github.com](mailto:bar2sek@users.noreply.github.com) | [linkedin.com/in/bar2sek](https://linkedin.com/in/bar2sek)

---

## Professional Summary

Cloud Infrastructure Leader and Enterprise Cloud Architect with 10+ years of experience designing, governing, automating, and modernizing enterprise technology environments across AWS, Azure, VMware, public-sector, financial-services, and agricultural organizations. Proven experience leading cloud engineering teams of 6–10 professionals, architecting multi-account and multi-agency landing zones, and executing large-scale modernization initiatives including the migration of 1,400+ VMware workloads to AWS.

Specializes in enterprise cloud architecture, Infrastructure as Code, cloud governance, platform engineering, DevSecOps, identity, networking, observability, and CI/CD automation. Experienced in establishing Terraform and GitHub-based engineering standards, cloud governance frameworks, architectural guardrails, and secure adoption patterns for emerging technologies including generative AI and Amazon Bedrock. Trusted partner to executive leadership, security teams, vendors, and consulting partners for translating business strategy into scalable, secure, and operationally sustainable cloud platforms.

---

## Core Competencies

- **Cloud & Platforms:** AWS (IAM / IAM Identity Center, SCPs, Control Tower guardrails, Security Hub, GuardDuty, CloudTrail, AWS Config, KMS, Organizations, Network Firewall, Secrets Manager, Transit Gateway), Microsoft Azure (AVD, Entra ID, Azure Policy, RBAC, Defender for Cloud, Key Vault, NSGs, Azure Firewall, Management Groups, Azure Monitor, Log Analytics, VMware Tanzu (BBR, BOSH, vSphere)
- **Diagramming & Whiteboarding:** Lucidchart, Miro, Microsoft Visio
- **Infrastructure as Code & Automation:** Terraform (Create deployment standard and module review under change control), Azure ARM templates (Authored and contributed to enterprise template library), Azure Bicep: (PoC for use vs Terraform), AWS CDK: Python variant (PoC for new AWS platform), PowerShell (Authored using Pester Test Driven Development), Bash (general linux system management)
- **CI/CD & DevOps:** GitHub, Azure DevOps, GitHub Actions, Concourse CI, Platform Automation, Docker
- **Networking & Security:** Aviatrix Transit Networking and Distributed Firewalls, Okta, Microsoft Entra ID (Azure AD)
- **Observability & Tools:** Prometheus, Grafana, Log Analytics, Selenium, Nerdio

---

## Experience

### State of Iowa – Department of Management
**Cloud Infrastructure Team Lead** | *April 2025 – Present*

#### Cloud Architecture & Enterprise Governance
- Designed and guided the cloud architecture for enterprise, multi-agency landing zones as part of the Contact Center Modernization initiative and AWS greenfield initiatives.
- Established cloud reference architectures, engineering standards, architectural decision processes, and reusable deployment patterns to ensure consistent implementation across independently operated agency environments.
- Established the enterprise AWS account hierarchy and OU strategy across dozens of state agencies, isolating security blast radius while enabling centralized policy enforcement, compliance auditing, and automated account provisioning.
- Authored, presented, and implemented a comprehensive multi-platform global naming and tagging standard adopted across all agencies, establishing a single source of truth for cloud resource management and reporting.
- Led infrastructure delivery for the Contact Center Modernization initiative and AWS greenfield implementation for Amazon Connect, collaborating with AWS Professional Services and ScaleCapacity to replace legacy call center infrastructure across four state agencies.
- Partnered with executive leadership, security, and compliance teams to establish the governance framework and deployment strategy for Amazon Bedrock, enabling secure generative AI adoption across state agency operations.
- Established cloud financial governance practices incorporating tagging compliance, account-level cost allocation, architectural cost reviews, forecasting, and workload optimization to improve visibility and accountability across agency cloud consumption.
#### Engineering Leadership & Cross-Functional Coordination
- Managed and coordinated a team of cloud engineers and technicians, strategically delegating complex implementation tasks based on individual skill sets, performance strengths, and project fit.
- Accelerated project delivery velocity and team cohesion by instituting structured daily stand-ups, hands-on working sessions, and routine project demonstrations, unifying disparate IT environments while successfully onboarding support personnel into a high-performing infrastructure unit.
- Translated complex multi-cloud architectures and enterprise roadmaps into clear, high-impact visual design artifacts for executive leadership, cross-agency stakeholders, and engineering teams.
- Executed AWS migration initiatives in partnership with AWS Professional Services, deploying AWS Migration Factory to rehost 1,400+ VMware virtual machines and core legacy applications for state agencies.
#### Technical Strategy, Tooling & Evaluation
- Conducted deep-dive architectural trade-off evaluations, specifically analyzing AWS Account Factory for Terraform (AFT) versus AWS Landing Zone Accelerator (LZA) to select and deploy the optimal platform for Day-2 operational longevity.
- Spearheaded the organization's Infrastructure as Code mandate by establishing Terraform as the global deployment standard while serving as GitHub Administrator to streamline change control and CI/CD pipelines.
- Led technical strategy for Aviatrix adoption, evangelizing enterprise cloud networking architectures to department leadership through structured cost-benefit models, risk-mitigation plans, distributed firewall strategies, and staffing alignment analyses.

---

### State of Iowa – Department of Health and Human Services
**Lead Platform Engineer** | *April 2021 – April 2025*

#### Azure Platform Modernization & Governance
- Spearheaded the planning, architectural design, and documentation of Azure platform and application landing zones in strict alignment with the Microsoft Cloud Adoption Framework (CAF).
- Designed, deployed, and managed Azure Virtual Desktop (AVD) environments utilizing native Azure tools and the Nerdio management platform to optimize secure remote operational workflows.
- Engineered enterprise identity federation and single sign-on (SSO) workflows, integrating Okta, Microsoft Entra ID (Azure AD), SAML authentication, and on-premises Active Directory.
- Led proof-of-concept (POC) evaluations for Aviatrix multi-cloud transit networking to enhance network visibility, security segmentation, and hybrid cloud connectivity.
- Designed and produced comprehensive architectural system diagrams and workflow visuals to communicate technical strategies across cross-functional state agency teams.

#### Tanzu Application Platform Engineering
- Orchestrated the greenfield configuration and deployment of VMware Tanzu Application Service (TAS) via BOSH on legacy on-premises vSphere infrastructure, partnering with VMware/Pivotal consultants to host refactored state assistance applications (e.g., Rent Reimbursement).
- Engineered CI/CD pipelines utilizing Concourse CI, Platform Automation, and GitOps workflows to automate core infrastructure configuration changes under strict pull-request and code-review controls.
- Drove team growth and engineering excellence by leading technical screening, onboarding, and structured mentorship for incoming engineering staff.

---

### Principal Financial Group
**Platform Engineer & Developer Support** | *July 2019 – April 2021*

- Supported platform workloads in AWS utilizing AWS CDK to develop and deploy reusable CloudFormation stacks, establishing automated GitHub Actions CI/CD infrastructure pipelines.
- Engineered Python and Docker-based platform microservices to extend Tanzu capabilities, including a highly available API gateway bridging cloud-native applications with legacy on-premises SOAP identity services.
- Automated CI/CD pipeline governance in Concourse CI, developing custom automation to enforce semantic versioning and Git tagging based on commit keywords for container images.
- Built containerized synthetic testing observability tooling using Python and Selenium to monitor authentication paths, alongside a translation layer routing Prometheus alerts directly to xMatters on-call platforms.
- Managed infrastructure lifecycles via BOSH on VMware vSphere IaaS with Ubuntu VMs, eliminating configuration drift across platform environments.
- Scripted platform disaster recovery automation utilizing BOSH Backup and Restore (BBR) targeting on-premises MinIO S3 storage buckets over NFS routing paths.
- Built and monitored real-time operational health dashboards and KPIs using Grafana and Prometheus for platform infrastructure and leadership visibility.
- Championed developer enablement by authoring architectural guides, markdown documentation, and deployment runbooks within Atlassian Confluence to accelerate application onboarding.

---

### Corteva Agriscience
**Cloud Engineer & Developer Support** | *October 2017 – July 2019*

- Engineered automation scripts using PowerShell and Pester unit testing for Azure Automation Runbooks, streamlining mass virtual machine backups, automated patching schedules, and systems management.
- Supported enterprise workloads in Azure, optimizing virtual machine performance for mission-critical SAP, HANA, Oracle, and SQL deployments running on Red Hat Enterprise Linux (RHEL) and Windows Server.
- Implemented infrastructure monitoring and alerting frameworks using Azure Monitor, Log Analytics, and Azure Alerts to proactively detect and remediate backup and system failures.
- Authored standard operating procedures, technical runbooks, and deployment guides in a centralized repository to establish consistent engineering best practices across vendors and internal teams.
- Onboarded and trained offshore engineering teams (including Accenture and Tata Consultancy Services / TCS), serving as the primary technical escalation point for enterprise cloud operations.

---

### Earlier Experience
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
- **Currently Pursuing:** AWS Certified Solutions Architect – Associate (SAA-C03)

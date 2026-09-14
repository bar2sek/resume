import subprocess
import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Ryan Bartusek - Resume</title>
<style>
  @page {
    size: letter;
    margin: 0.42in 0.48in;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    font-size: 8.8pt;
    line-height: 1.34;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  
  /* Header */
  .header {
    text-align: center;
    border-bottom: 2px solid #0f172a;
    padding-bottom: 5px;
    margin-bottom: 8px;
  }
  .header h1 {
    font-size: 20pt;
    font-weight: 800;
    letter-spacing: -0.5px;
    color: #0f172a;
    text-transform: uppercase;
    margin-bottom: 1px;
  }
  .header .subtitle {
    font-size: 9.6pt;
    font-weight: 700;
    color: #2563eb;
    letter-spacing: 0.2px;
    margin-bottom: 4px;
  }
  .header .contact-row {
    font-size: 8.4pt;
    color: #475569;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
  }
  .header .contact-row a {
    color: #475569;
    text-decoration: none;
  }
  .header .contact-row .separator {
    color: #cbd5e1;
  }

  /* Section Styles */
  .section {
    margin-bottom: 9px;
  }
  .section-title {
    font-size: 9.8pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #0f172a;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 2px;
    margin-bottom: 5px;
  }

  /* Summary */
  .summary-text {
    color: #334155;
    text-align: justify;
    margin-bottom: 4px;
  }
  .summary-text:last-child {
    margin-bottom: 0;
  }

  /* Competencies Grid */
  .competencies-list {
    list-style: none;
  }
  .competencies-list li {
    margin-bottom: 2.5px;
    position: relative;
    padding-left: 12px;
    color: #334155;
  }
  .competencies-list li::before {
    content: "▪";
    position: absolute;
    left: 0;
    color: #2563eb;
    font-size: 8pt;
    top: -0.5px;
  }
  .competencies-list strong {
    color: #0f172a;
    font-weight: 700;
  }

  /* Experience Jobs */
  .job-block {
    margin-bottom: 8px;
    break-inside: avoid;
    page-break-inside: avoid;
  }
  .job-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 1px;
  }
  .company-name {
    font-size: 9.5pt;
    font-weight: 800;
    color: #0f172a;
  }
  .job-title-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 3.5px;
  }
  .job-title {
    font-size: 8.8pt;
    font-weight: 700;
    color: #2563eb;
  }
  .job-dates {
    font-size: 8.2pt;
    font-weight: 600;
    color: #64748b;
  }

  /* Bullet Lists */
  .bullet-list {
    list-style: none;
  }
  .bullet-list li {
    position: relative;
    padding-left: 12px;
    margin-bottom: 2.5px;
    color: #334155;
    text-align: justify;
  }
  .bullet-list li::before {
    content: "•";
    position: absolute;
    left: 0;
    color: #0284c7;
    font-weight: bold;
    font-size: 9pt;
    top: -0.5px;
  }
  .bullet-list li strong {
    color: #0f172a;
  }

  /* Page Break Helper */
  .page-break {
    page-break-before: always;
    break-before: page;
  }

  /* Two Column Section for Bottom */
  .bottom-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    break-inside: avoid;
    page-break-inside: avoid;
  }
  .bottom-grid .section-title {
    margin-bottom: 4px;
  }

  .earlier-exp-list, .edu-list, .cert-list {
    list-style: none;
  }
  .earlier-exp-list li, .edu-list li, .cert-list li {
    position: relative;
    padding-left: 10px;
    margin-bottom: 2px;
    color: #334155;
    font-size: 8.4pt;
  }
  .earlier-exp-list li::before, .edu-list li::before, .cert-list li::before {
    content: "▪";
    position: absolute;
    left: 0;
    color: #64748b;
    font-size: 7.5pt;
    top: -0.5px;
  }
  .earlier-exp-list strong, .edu-list strong, .cert-list strong {
    color: #0f172a;
  }
</style>
</head>
<body>

  <!-- Page 1 -->
  <div class="header">
    <h1>Ryan Bartusek</h1>
    <div class="subtitle">Enterprise Cloud Architecture | Cloud Platform Engineering</div>
    <div class="contact-row">
      <span>Des Moines, IA</span>
      <span class="separator">|</span>
      <span><a href="mailto:bar2sek@users.noreply.github.com">bar2sek@users.noreply.github.com</a></span>
      <span class="separator">|</span>
      <span><a href="https://linkedin.com/in/bar2sek">linkedin.com/in/bar2sek</a></span>
    </div>
  </div>

  <div class="section">
    <div class="section-title">Professional Summary</div>
    <p class="summary-text">
      Cloud Infrastructure Leader and Enterprise Cloud Architect with 10+ years of experience driving cloud platform maturity across public-sector, financial, and enterprise domains. Proven track record leading engineering teams of 6–10, architecting enterprise multi-account AWS environments across production and non-production, and operationalizing statewide Terraform mandates through engineer enablement and automated change-control governance.
    </p>
    <p class="summary-text">
      Specializes in aligning strategic business goals with scalable cloud foundations, automated account vending pipelines, and Infrastructure as Code (IaC) delivery models. Demonstrated success establishing architectural standards, multi-environment security guardrails, and modern DevSecOps practices that accelerate developer velocity while maintaining strict compliance and operational resilience. Trusted advisor to executive leadership, security teams, and delivery partners for translating organizational vision into scalable, secure, and sustainable cloud platforms.
    </p>
  </div>

  <div class="section">
    <div class="section-title">Core Competencies</div>
    <ul class="competencies-list">
      <li><strong>Cloud & Platforms:</strong> AWS (Organizations, Control Tower, SCPs, IAM Identity Center, Bedrock, Connect, Transit Gateway, Security Hub, GuardDuty, KMS, Config, CloudTrail), Microsoft Azure (AVD, Entra ID, Azure Policy, Defender for Cloud, Key Vault, Azure Firewall, Management Groups, Log Analytics), VMware Tanzu (TAS, BOSH, BBR, vSphere)</li>
      <li><strong>Infrastructure as Code & Automation:</strong> Terraform (Enterprise Deployment, Modules, & Standards), AWS CDK (Python), Azure Bicep & ARM Templates, PowerShell (Pester TDD), Bash, GitOps</li>
      <li><strong>CI/CD & DevSecOps:</strong> GitHub & GitHub Actions (Org Administrator), Azure DevOps, Concourse CI, Docker</li>
      <li><strong>Networking & Security:</strong> Aviatrix Transit Networking & Distributed Firewalls, SAML / SSO Identity Federation (Okta, Entra ID, Active Directory), Role-Based Access Control (RBAC)</li>
      <li><strong>Observability & Operations:</strong> Prometheus, Grafana, Azure Monitor, Log Analytics, Nerdio Manager, Selenium</li>
      <li><strong>Diagramming & Design:</strong> Lucidchart, Miro, Microsoft Visio</li>
    </ul>
  </div>

  <div class="section">
    <div class="section-title">Experience</div>
    
    <div class="job-block">
      <div class="job-header">
        <span class="company-name">State of Iowa – Department of Management</span>
        <span class="job-dates">April 2025 – Present</span>
      </div>
      <div class="job-title-row">
        <span class="job-title">Cloud Infrastructure Team Lead</span>
      </div>
      <ul class="bullet-list">
        <li><strong>Enterprise Multi-Account & OU Hierarchy:</strong> Designed and governed an enterprise-scale AWS multi-account topology across state agencies, structuring functional <strong>Security, Core Infrastructure, Workloads (Prod / Non-Prod / Sandbox), Exceptions, and Suspended OUs</strong>; enforced strict blast-radius isolation, baseline security controls (CloudTrail, Config, Security Hub, GuardDuty), and hierarchical <strong>Service Control Policies (SCPs)</strong>.</li>
        <li><strong>Automated Account Vending & Baselines:</strong> Architected and deployed <strong>AWS Account Factory for Terraform (AFT)</strong> and AWS Control Tower, orchestrating GitOps-driven account vending pipelines via GitHub Actions and AWS CodePipeline to automate zero-touch provisioning with baseline guardrails, IAM Identity Center, transit networking, and OU policy inheritance.</li>
        <li><strong>Architectural Decisions & Standards:</strong> Led technical trade-off evaluations (e.g., <strong>Terraform vs. Azure Bicep & CloudFormation</strong>) and documented decision rationale to establish Terraform and policy-as-code as enterprise standards across multi-cloud environments; built modular reference architectures that accelerated agency project intake.</li>
        <li><strong>FinOps & Cost Governance:</strong> Evaluated <strong>Apptio Cloudability</strong> and AWS Cost Management tools to establish enterprise tagging governance, cost attribution, and multi-agency budget visibility.</li>
        <li><strong>Large-Scale Cloud Migration Support:</strong> Led the infrastructure engineering team collaborating with AWS Professional Services on statewide migration initiatives, utilizing AWS Migration Factory to rehost <strong>1,400+ VMware virtual machines</strong> and core legacy applications for state agencies.</li>
        <li><strong>GenAI & Emerging Tech Governance:</strong> Partnered with executive leadership, security, and compliance teams to establish the architecture and governance framework for <strong>Amazon Bedrock</strong>, enabling secure generative AI adoption across state operations.</li>
        <li><strong>Contact Center Modernization:</strong> Led infrastructure delivery and multi-agency greenfield deployment of <strong>Amazon Connect</strong> in collaboration with AWS Professional Services and ScaleCapacity, replacing legacy telephony across four state agencies.</li>
        <li><strong>Engineering Leadership & Governance:</strong> Managed and coordinated a team of <strong>6–10 cloud engineers and technicians</strong>; instituted structured agile ceremonies, elevated team delivery velocity, and served as GitHub Administrator for change control.</li>
        <li><strong>Multicloud Networking & Security Strategy:</strong> Spearheaded technical strategy and executive buy-in for <strong>Aviatrix</strong> multicloud transit networking and distributed firewalls, delivering centralized visibility, hybrid connectivity, and advanced security segmentation.</li>
      </ul>
    </div>
  </div>

  <!-- Page 2 -->
  <div class="page-break"></div>

  <div class="section">
    <div class="job-block">
      <div class="job-header">
        <span class="company-name">State of Iowa – Department of Health and Human Services</span>
        <span class="job-dates">April 2021 – April 2025</span>
      </div>
      <div class="job-title-row">
        <span class="job-title">Lead Platform Engineer</span>
      </div>
      <ul class="bullet-list">
        <li><strong>Azure Platform & Landing Zones:</strong> Spearheaded architectural design, governance, and deployment of enterprise Azure landing zones in strict alignment with the Microsoft Cloud Adoption Framework (CAF).</li>
        <li><strong>Virtual Desktop Infrastructure (AVD):</strong> Designed, deployed, and managed Azure Virtual Desktop (AVD) environments utilizing native Azure services and the Nerdio management platform to optimize secure remote access for statewide personnel.</li>
        <li><strong>Identity Federation & Access Governance:</strong> Engineered enterprise identity federation and SSO workflows, integrating Okta, Microsoft Entra ID (Azure AD), SAML authentication, and on-premises Active Directory; implemented least-privilege RBAC, conditional access policies, and centralized authorization across hybrid environments.</li>
        <li><strong>Multicloud Networking POC:</strong> Led proof-of-concept (POC) evaluations for Aviatrix multicloud transit networking to enhance network visibility, security segmentation, and hybrid cloud connectivity.</li>
        <li><strong>PaaS Platform Engineering:</strong> Orchestrated greenfield configuration and deployment of VMware Tanzu Application Service (TAS) via BOSH on legacy on-premises vSphere infrastructure, partnering with VMware consultants to host refactored state assistance applications (e.g., Rent Reimbursement).</li>
        <li><strong>CI/CD Automation & Mentorship:</strong> Built CI/CD pipelines utilizing Concourse CI, Platform Automation, and GitOps workflows under strict pull-request controls; drove team growth through technical screening, onboarding, and structured mentorship.</li>
      </ul>
    </div>

    <div class="job-block">
      <div class="job-header">
        <span class="company-name">Principal Financial Group</span>
        <span class="job-dates">July 2019 – April 2021</span>
      </div>
      <div class="job-title-row">
        <span class="job-title">Platform Engineer & Developer Support</span>
      </div>
      <ul class="bullet-list">
        <li><strong>AWS IaC & CI/CD Automation:</strong> Supported platform workloads in AWS utilizing AWS CDK (Python) to develop and deploy reusable CloudFormation stacks, establishing automated GitHub Actions CI/CD infrastructure pipelines.</li>
        <li><strong>Microservices & API Gateway:</strong> Engineered Python and Docker-based platform microservices to extend Tanzu capabilities, including a highly available API gateway bridging cloud-native applications with legacy on-premises SOAP identity services.</li>
        <li><strong>Pipeline Governance:</strong> Automated CI/CD pipeline governance in Concourse CI, developing custom automation to enforce semantic versioning and Git tagging based on commit keywords for container images.</li>
        <li><strong>Synthetic Monitoring & Observability:</strong> Built containerized synthetic testing observability tooling using Python and Selenium to monitor authentication paths; created real-time operational health dashboards in Grafana and Prometheus with xMatters alerting integration.</li>
        <li><strong>Platform Operations & Disaster Recovery:</strong> Managed infrastructure lifecycles via BOSH on VMware vSphere IaaS with Ubuntu VMs; scripted automated disaster recovery using BOSH Backup and Restore (BBR) targeting on-premises MinIO S3 storage buckets over NFS.</li>
        <li><strong>Developer Enablement:</strong> Authored architectural guides, markdown documentation, and deployment runbooks within Atlassian Confluence to accelerate engineering team onboarding.</li>
      </ul>
    </div>

    <div class="job-block">
      <div class="job-header">
        <span class="company-name">Corteva Agriscience</span>
        <span class="job-dates">October 2017 – July 2019</span>
      </div>
      <div class="job-title-row">
        <span class="job-title">Cloud Engineer & Developer Support</span>
      </div>
      <ul class="bullet-list">
        <li><strong>Automation & Test-Driven Development:</strong> Engineered automation scripts using PowerShell and Pester unit testing for Azure Automation Runbooks, streamlining mass virtual machine backups, automated patching schedules, and systems management.</li>
        <li><strong>Enterprise Workload Optimization:</strong> Supported enterprise workloads in Azure, optimizing virtual machine performance for mission-critical SAP, HANA, Oracle, and SQL deployments running on Red Hat Enterprise Linux (RHEL) and Windows Server.</li>
        <li><strong>Monitoring & Alerting Frameworks:</strong> Implemented infrastructure monitoring and alerting frameworks using Azure Monitor, Log Analytics, and Azure Alerts to proactively detect and remediate backup and system failures.</li>
        <li><strong>Engineering Best Practices:</strong> Authored standard operating procedures, technical runbooks, and deployment guides in a centralized repository to establish consistent engineering best practices across vendors and internal teams.</li>
        <li><strong>Offshore Team Enablement:</strong> Onboarded and trained offshore engineering teams (including Accenture and TCS), serving as the primary technical escalation point for enterprise cloud operations.</li>
      </ul>
    </div>
  </div>

  <div class="section" style="margin-bottom: 6px;">
    <div class="section-title">Earlier Experience</div>
    <ul class="earlier-exp-list" style="display: grid; grid-template-columns: 1fr 1fr; gap: 2px 14px;">
      <li><strong>Lean TECHniques</strong> | Software Developer (2016 – 2017)</li>
      <li><strong>EMC Insurance</strong> | Software Developer (2016)</li>
      <li><strong>LightEdge Solutions</strong> | Data Center Technician (2014 – 2016)</li>
      <li><strong>IdentoGO by MorphoTrust</strong> | Support Technician (2011 – 2013)</li>
    </ul>
  </div>

  <div class="bottom-grid">
    <div class="section" style="margin-bottom: 0;">
      <div class="section-title">Education</div>
      <ul class="edu-list">
        <li><strong>Iowa State University</strong> – BA, Visual Studies</li>
        <li><strong>Des Moines Area Community College</strong> – AS, Business Information Systems</li>
      </ul>
    </div>

    <div class="section" style="margin-bottom: 0;">
      <div class="section-title">Certifications</div>
      <ul class="cert-list">
        <li><strong>Aviatrix ACE</strong> – Multicloud Network Professional</li>
        <li><strong>Aviatrix ACE</strong> – Multicloud Network Associate</li>
        <li><strong>Microsoft Certified</strong> – Azure Fundamentals (AZ-900) & Data (DP-900)</li>
        <li><strong>AWS Certified Solutions Architect – Associate</strong> <em>(Expected 2026)</em></li>
      </ul>
    </div>
  </div>

</body>
</html>
"""

with open("resume_preview.html", "w") as f:
    f.write(html_content)

import tempfile
import shutil

chrome_path = os.environ.get(
    "CHROME_PATH",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if os.path.exists("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    else (
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        if os.path.exists("/Applications/Brave Browser.app/Contents/MacOS/Brave Browser")
        else (shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser") or "google-chrome")
    )
)
pdf_output = "Ryan_Bartusek_Resume_2026v7.pdf"

temp_profile = tempfile.mkdtemp()

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    f"--user-data-dir={temp_profile}",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_output}",
    os.path.abspath("resume_preview.html")
]

print("Rendering PDF...")
try:
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
    if res.returncode == 0:
        print(f"Successfully generated {pdf_output}")
    else:
        print(f"Error (code {res.returncode}): {res.stderr}")
except subprocess.TimeoutExpired:
    print("Error: Rendering timed out.")
finally:
    shutil.rmtree(temp_profile, ignore_errors=True)

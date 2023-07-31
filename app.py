from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Manish Krishna Ramakrishnan"
PAGE_ICON = ":wave:"
NAME = "Manish Krishna Ramakrishnan"
DESCRIPTION = """
DevOps Engineer.
"""
EMAIL = "manizkrish96@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=":roll_of_paper:  Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write(":mailbox:", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 3.5 Years experience in creating cloud infrastructure and deploying on web
- ✔️ Strong hands on experience in Aws Service and DevOps Tools
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- :cloud: Aws Services: EC2, S3, VPC, IAM, RDS, ELB, AUTO SCALING, CLOUDFRONT, CLOUDWATCH, SQS,SNS
- :robot: DevOps Tools: GITHUB, JENKINS, DOCKER, KUBERNETES, ANSIBLE, TERRAFORM, SONARQUBE, NEXUS
- :desktop_computer: Operating System: LINUX, UBUNTU, WINDOWS
- :bank: Databases: MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**DevOps Engineer | Mindtree**")
st.write("02/2020 - Present")
st.write(
    """
LIFE INSURANCE CLIENT - MIRAE ASSET
ROLES AND RESPONSIBILITIES
-  :eight_pointed_black_star: Having experience in Cloud Infrastructure using Amazon Web Services (AWS). Leveraging various services such as EC2, S3, EFS, IAM, Load Balancer, Auto Scaling, VPC, Route 53, CloudFront, CloudWatch, and RDS. I have used EBS and EFS as per requirements to ensure efficient storage solutions.
-  :eight_pointed_black_star:Worked on creating IAM user groups, and defining roles policies.
-  :eight_pointed_black_star:Creating/Managing backup and recovery through AMI's for critical Ec2 instances and Snapshots.
-  :eight_pointed_black_star:Collaborated with development, QA and IT operations staff to enhance software productivity.
-  :eight_pointed_black_star:Significant experience on Git as a Version Control System focusing on code management through GitHub repositories.
-  :eight_pointed_black_star:Furthermore, I have hands-on experience on robust CI/CD pipelines using Jenkins. Worked with DOCKER and KUBERNETES for deployment instrumental in transitioning from a monolithic architecture to a microservices architecture.
-  :eight_pointed_black_star:I have demonstrated in utilizing Sona type Nexus repositories for efficient management of artifacts and dependencies.
-  :eight_pointed_black_star:I possess strong skill in creating and managing the infrastructure using TERRAFORM and ANSIBLE.

HEALTHCARE CLIENT - SeaSpine
ROLES AND RESPONSIBILITIES
-  :eight_pointed_black_star:Worked extensively on AWS services like Ec2, Elb, Auto Scaling, EBS, S3, Vpc, IAM, Cloudwatch.
-  :eight_pointed_black_star:Managed and created users and group accounts with required roles and policy restrictions using IAM service.
-  :eight_pointed_black_star:Installed and setup Web servers like Apache and Tomcat.
-  :eight_pointed_black_star:Integrated and configured CI/CD through jenkins plug-in, created master-slave configuration for parallel builds.
-  :eight_pointed_black_star:Worked on Docker containers for different environments.
-  :eight_pointed_black_star:Well-versed in Linux administration duties, including installation and maintenance tasks. Overall, I bring extensive experience and knowledge in AWS cloud and DevOps tools.

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Desktop Support | Mindtree**")
st.write("01/2018 - 02/2022")
st.write(
    """
-  :eight_pointed_black_star:Respond to user tickets related to hardware, software, and networking problems.
-  :eight_pointed_black_star:Guide users through the installation process of applications and computer peripherals.
-  :eight_pointed_black_star:Perform remote troubleshooting to address issues without physical access to the computer.
-  :eight_pointed_black_star:Explore different solutions and pathways until a resolution is found.
-  :eight_pointed_black_star:Customize desktop applications to align with the specific needs of users.
-  :eight_pointed_black_star:Maintain a log of technical issues and their corresponding solutions for future reference.

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**CNC Operator | Gobal Technology**")
st.write("04/2015 - 01/2018")
st.write(
    """
-  :eight_pointed_black_star:Well versed in programming, setting-up and operating a CNC Machine.
-  :eight_pointed_black_star:Set-up and manage CNC machines to perform different jobs including drilling and grinding.
-  :eight_pointed_black_star:Translate engineering drawings and requirements into program for production.
"""
)


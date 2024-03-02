import pandas as pd
import random

# Expanded options for each column with added companies
titles = [
    'Software Engineer', 'Data Scientist', 'Product Manager', 'Graphic Designer', 'Systems Administrator',
    'Cybersecurity Analyst', 'Network Engineer', 'UI/UX Designer', 'Cloud Solutions Architect', 'Technical Writer',
    'DevOps Engineer', 'Database Administrator', 'Mobile Developer', 'SEO Specialist', 'AI Research Scientist'
]
descriptions = [
    'Develop and maintain software applications using a variety of programming languages.',
    'Analyze data to identify trends and insights that can help guide business decisions.',
    'Oversee the development and launch of products, working closely with engineering and marketing teams.',
    'Create visual content for digital and print media, ensuring it aligns with brand guidelines.',
    'Manage and maintain the company’s IT infrastructure, ensuring systems are secure and run smoothly.',
    'Protect company’s computer networks and systems by identifying and solving any security breaches or potential threats.',
    'Design and implement new solutions to improve the efficiency and security of the company’s network infrastructure.',
    'Design the user interface and experience for digital products, ensuring they are intuitive and user-friendly.',
    'Design and deploy dynamically scalable and reliable applications on cloud platforms, ensuring optimal performance.',
    'Create technical documentation for product features, user manuals, and other documents to facilitate clear communication.',
    'Implement automation tools and frameworks (CI/CD pipelines) to facilitate the rapid development of applications.',
    'Manage and support database architecture, including performance, integrity, and security of the data.',
    'Design and build mobile applications for iOS or Android platforms, ensuring a seamless user experience.',
    'Optimize website content for search engines to increase visibility and traffic.',
    'Conduct research and experiments in artificial intelligence to develop novel solutions and advancements.'
]
requirements = [
    'Bachelor’s degree in Computer Science, 3+ years of programming experience, proficient in Python and Java.',
    'Degree in Statistics or related field, proficient in R and Python, experience with machine learning algorithms.',
    'Bachelor’s degree, 5+ years in product management, strong project management skills, experience in Agile methodologies.',
    'Bachelor’s degree in Graphic Design, proficient in Adobe Creative Suite, strong portfolio of previous work.',
    'Degree in Information Technology, 3+ years of experience with network administration, knowledge of cloud services.',
    'Bachelor’s degree in Information Security, proficient in security protocols, 2+ years of experience in cybersecurity.',
    'Bachelor’s degree in Computer Science, experience with network protocols and standards, certification in networking preferred.',
    'Degree in Design or related field, experience with design software (Sketch, Figma), understanding of web technologies.',
    'Degree in Computer Science, experience with AWS/GCP/Azure, understanding of software development and cloud computing.',
    'Degree in Technical Writing, English, or related field, experience in technical writing, ability to explain complex information.',
    'Experience with scripting languages, knowledge of automation tools, and experience with systems and IT operations.',
    'Experience with database management, knowledge of SQL and NoSQL databases, and familiarity with data backup, recovery, and security.',
    'Bachelor’s degree in Computer Science, experience in mobile development frameworks, and a strong understanding of UI/UX design.',
    'Proven experience in SEO strategies, understanding of web analytics, and familiarity with content management systems.',
    'Ph.D. in Computer Science or related field, experience with machine learning frameworks, and a strong publication record in AI.'
]
locations = [
    'New York, NY', 'San Francisco, CA', 'Los Angeles, CA', 'Chicago, IL', 'Austin, TX',
    'Dallas, TX', 'Boston, MA', 'Seattle, WA', 'Denver, CO', 'Atlanta, GA',
    'San Diego, CA', 'Portland, OR', 'Miami, FL', 'Washington, DC', 'Minneapolis, MN',
    'Raleigh, NC', 'Detroit, MI', 'Nashville, TN', 'Salt Lake City, UT', 'Orlando, FL'
]
companies = [
    'Tech Innovations Inc.', 'Global Solutions Ltd.', 'NextGen Technologies', 'Creative Minds LLC',
    'GreenTech Solutions', 'Data Analytics Corp.', 'Cloud Services International', 'Digital Dynamics',
    'EcoTech Enterprises', 'Future Horizons', 'IntelliDesign Studios', 'Quantum Computing Inc.',
    'Virtual Reality Ventures', 'AI Pioneers', 'CyberSecurity Pros', 'Blockchain Basics LLC', 'Smart Solutions',
    'Renewable Tech Co.', 'Software Giants', 'Tech Trailblazers Inc.'
]

# Generate a large number of job listings
num_listings = 1000  # Adjust as needed
data = {
    'company': [random.choice(companies) for _ in range(num_listings)],
    'job title': [random.choice(titles) for _ in range(num_listings)],
    'job description': [random.choice(descriptions) for _ in range(num_listings)],
    'requirements': [random.choice(requirements) for _ in range(num_listings)],
    'location': [random.choice(locations) for _ in range(num_listings)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to a CSV file
file_path = 'job_listings.csv'
df.to_csv(file_path, index=False)

print(f"CSV file with {num_listings} expanded job listings created at: {file_path}")

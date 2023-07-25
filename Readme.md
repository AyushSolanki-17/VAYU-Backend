         
# VAYU
## Overview
Project COPD Diagnosing Application (VAYU): The project "Vayu" utilises AI and machine learning to diagnose COPD. As
a part of the development team, I created supervised learning models using classification algorithms for the ABG and PFT test
outcomes. I also implemented image processing techniques to classify respiratory problems using chest x-ray image datasets.
Additionally, stethoscope audio capturing and detection of COPD from heartbeat audio using audio processing and deep
learning were developed. A medical health chatbot was also created to chat in English and Hindi. The user integrated the
machine learning models with Django and created REST APIs. Furthermore, the user developed a Flutter application for the
user interface and utilised blockchain to store all medical records of the tests. Web application was deployed on Google Cloud.

## Table of Contents

<ol>
    <li><a href="#Abstract">Abstract</a></li>
    <li><a href="#About-UIA">About Unesco India Africa Hackathon</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#Technology">Technology</a></li>
    <li><a href="#Screenshots">Screenshots</a></li>
    <li><a href="#Documentation">Full Documentation</a></li>
    <li><a href="#Further-Enhancements">Further Enhancements</a></li>
    
 </ol>
 
## Abstract

With increased pollution and some unsuitable human actions that contribute to environmental deterioration, new varieties of illness, virus, bacterium, and so on are being found in contemporary times. These illnesses might develop into pandemics. 
The condition known as chronic obstructive pulmonary disease (COPD) is one of the respiratory disorders.
Based on epidemiological statistics, COPD will rank among the world's top causes of mortality and a significant contributor to disability. 
The mortality rate is still high despite the fact that methods and tools have been created to combat COPD measures. 
VAYU is our proposed system for monitoring COPD patients and increasing COPD awareness. 
The primary function of VAYU is to identify ACID-BASE problems in a patient with COPD. 
The sophisticated machine learning algorithms used by VAYU may identify many disorders based on blood parameters. 
Blood parameters must be evaluated, and the entire medication procedure is predicated on correctly identifying a specific condition from a blood sample. 
Additionally, VAYU uses neural networks for computer vision and image processing to recognise coughs and respiratory issues.
A routine user of VAYU can learn whether they have COPD by taking a test that looks at their regular symptoms. 
Doctors, lab technicians, and patients can all access various VAYU services.
A chatbot that will be taught to serve as a VIRTUAL DOCTOR is also a part of VAYU. 
The goal of VAYU is to provide a whole end-to-end solution, from the diagnosis of COPD through the treatment of its diseases. 

## About UIA


<p align="center"><img src="https://user-images.githubusercontent.com/55245862/205508044-e43024b4-3c92-4ab9-9f6b-e3c6038205a6.jpg" height="200" width="300"></p>

The UNESCO INDIA – AFRICA Hackathon is an annual 36 hours event that brings together students, educators, teachers, and the research community of India and its African partners to tackle the common challenges faced by their countries and serves as a facilitator for cultural amalgamation.

The UNESCO INDIA – AFRICA Hackathon provides a suitable platform allowing young innovators to come together and find solutions for social, environmental and technical problems faced by the collaborating nations. It serves as the foundation for creating potential start-ups with the potential to transform the world. It allows the participating students to unleash their creativity and explore new technologies to solve real-world problems under the guidance of experts - thus, spearheading business innovation in the modern world.

Collaboration of the student teams working together to solve shared problems opens the doors to cultural assimilation by introducing students and their mentors to methods, values and manners different from their own.

The Hackathon also serves as a symbol of the close relation cherished by India and its African counterparts and embodies the spirit of collaboration - bringing them together to solve problems for the betterment of humankind.


## Features

The following are some of the features of the VAYU application.

📑Interpretation of Blood Reports Using PDF Scanning (PDF Scanning, Machine Learning)

🩻X-RAY Imaging for Respiratory Issues (Image Processing)

🩺COPD prognosis using Heartbeat audio (Audio Processing, Deep Learning)

🤖English and Hindi chatbots (NLTK)

⛓️Reports based on blockchain technology

👨‍⚕️Connect with your doctor.

## Technology

### Backend
<table>
    <tr>
        <td><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="Python" /></td>
        <td><img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="Tensorflow" /></td>
        <td><img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit Learn" /></td>
    </tr>
    <tr>
        <td><img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" alt="Django" /></td>
        <td><img src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white" alt="Django REST" /></td>
        <td><img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="Postgres SQL" /></td>
    </tr>
</table>

### Frontend
<table>
    <tr>
        <td><img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white" alt="Flutter" /></td>
        <td><img src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white" alt="Dart" /></td>
        <td><img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" /></td>
    </tr>
    
</table>      
         
## Screenshots
<table>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/61615248/255895857-a33f898a-ff9f-40a9-ba19-bf7b68ed5f9d.jpg" alt="Screenshot1" /></td>
        <td><img src="https://user-images.githubusercontent.com/61615248/255895852-dcee6f11-1b22-44d5-ad07-d0c50adf31e9.jpg" alt="Screenshot2" /></td>
        <td><img src="https://user-images.githubusercontent.com/61615248/255895848-920278e3-ad9d-4fd2-9e00-528cc779b643.jpg" alt="Screenshot3" /></td>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/61615248/255895840-b1ade3a4-85fa-474f-8ddc-a9a7e63e22bd.jpg" alt="Screenshot4" /></td>
        <td><img src="https://user-images.githubusercontent.com/61615248/255895831-cf20feb7-6800-46ff-b7e1-9a6ba98ff854.jpg" alt="Screenshot5" /></td>
        <td><img src="https://user-images.githubusercontent.com/61615248/255895822-1685fb02-360f-4dfc-b306-e5e1c55b7e22.jpg" alt="Screenshot6" /></td>
    </tr>
</table>

## Documentation
<a href="https://drive.google.com/file/d/1QAwxY5uiZKHYMBSroJj0mDrHXjmNwQOn/view?usp=sharing">Link to Documentation</a>

## Further Enhancements

- [ ] More research and features

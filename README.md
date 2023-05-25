<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/5.5.3/collection/components/icon/icon.min.css" integrity="sha512-PlY2fG4xU/9Hx8yA7fObndTdXcGz7Bj5SGJL8Xk8pbxzqgSzxH9/Md2M0r3IgXjLHJzKuehw8T2k6fENHyHgeA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <style>
    /* Global Styles */
    * {
      box-sizing: border-box;
    }

    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }

    h1, h2, h3, h4, h5 {
      margin: 0;
    }

    p {
      margin: 0;
      line-height: 1.5;
    }

    a {
      text-decoration: none;
      color: #000;
    }

    ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }

    /* Container Styles */
    .container {
      max-width: 900px;
      margin: 0 auto;
      padding: 20px;
    }

    /* Header Styles */
    .header {
      text-align: center;
      margin-bottom: 20px;
    }

    .header h1 {
      font-size: 24px;
      margin-bottom: 10px;
    }

    .header p {
      font-size: 18px;
    }

    /* Social Links Styles */
    .social-list {
      display: flex;
      justify-content: center;
      margin-bottom: 20px;
    }

    .social-item {
      margin: 0 10px;
    }

    /* About Section Styles */
    .about-section {
      margin-bottom: 20px;
    }

    .about-section h2 {
      font-size: 20px;
      margin-bottom: 10px;
    }

    /* Service Section Styles */
    .service-section {
      margin-bottom: 20px;
    }

    .service-section h3 {
      font-size: 20px;
      margin-bottom: 10px;
    }

    .service-item {
      display: flex;
      align-items: center;
      margin-bottom: 10px;
    }

    .service-icon-box {
      margin-right: 10px;
      font-size: 24px;
    }

    /* Contact Section Styles */
    .contact-section {
      text-align: center;
    }

    .contact-section h2 {
      font-size: 20px;
      margin-bottom: 10px;
    }

    .contact-section a {
      color: #ff0000;
      font-weight: bold;
    }
  </style>
  <title>GitHub About Me</title>
</head>
<body>
  <div class="container">
    <header class="header">
      <h1 class="name" title="Doğukan Sahil">Doğukan Sahil</h1>
      <p class="title">Genetics and Bioengineer 👨🏽‍🔬</p>
    </header>

    <ul class="social-list">
      <li class="social-item">
        <a href="https://github.com/dogukansahil" target="_blank" rel="noopener noreferrer">
          <i class="icon ion-logo-github"></i>
        </a>
      </li>
      <li class="social-item">
        <a href="https://www.linkedin.com/in/dogukansahil" target="_blank" rel="noopener noreferrer">
          <i class="icon ion-logo-linkedin"></i>
        </a>
      </li>
      <li class="social-item">
        <a href="https://twitter.com/dogukansahil" target="_blank" rel="noopener noreferrer">
          <i class="icon ion-logo-twitter"></i>
        </a>
      </li>
    </ul>

    <section class="about-section">
      <h2>About Me</h2>
      <p>
        Hello! I'm Doğukan Sahil, a passionate Genetics and Bioengineer. I have a strong interest in genetic research and the application of bioengineering in healthcare. I believe that combining biology with engineering principles can revolutionize the medical field and improve people's lives. In my free time, I enjoy coding and contributing to open source projects related to genetics and bioengineering.
      </p>
    </section>

    <section class="service-section">
      <h3>Services</h3>
      <ul>
        <li class="service-item">
          <div class="service-icon-box">
            <i class="icon ion-md-code-working"></i>
          </div>
          <div class="service-description">
            <h4>Web Development</h4>
            <p>I have experience in front-end and back-end web development. I enjoy building user-friendly and responsive websites using modern technologies like HTML, CSS, JavaScript, and frameworks like React and Node.js.</p>
          </div>
        </li>
        <li class="service-item">
          <div class="service-icon-box">
            <i class="icon ion-md-bug"></i>
          </div>
          <div class="service-description">
            <h4>Bioinformatics</h4>
            <p>With my background in genetics and bioengineering, I can also provide bioinformatics services. I have expertise in analyzing genetic data, performing sequence alignments, and developing computational tools for genetic research.</p>
          </div>
        </li>
        <li class="service-item">
          <div class="service-icon-box">
            <i class="icon ion-md-medical"></i>
          </div>
          <div class="service-description">
            <h4>Medical Writing</h4>
            <p>Being knowledgeable in genetics and bioengineering, I can offer medical writing services. I can write clear and concise scientific articles, research papers, and documentation related to genetics, bioengineering, and healthcare.</p>
          </div>
        </li>
      </ul>
    </section>

    <section class="contact-section">
      <h2>Contact Me</h2>
      <p>If you'd like to get in touch with me, feel free to send me an email at <a href="mailto:dogukan@example.com">dogukan@example.com</a> or connect with me on <a href="https://www.linkedin.com/in/dogukansahil" target="_blank" rel="noopener noreferrer">LinkedIn</a>.</p>
    </section>
  </div>
</body>
</html>

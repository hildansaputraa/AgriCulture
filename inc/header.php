<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <title>SignLearn</title>
    <meta name="description" content="SignLearn - An innovative platform for learning and collaboration.">
    <meta name="keywords" content="learning, education, online, collaboration, SignLearn">

    <!-- Favicons -->
    <link href="src/logohead.png" rel="icon">

    <!-- Fonts -->
    <link href="https://fonts.googleapis.com" rel="preconnect">
    <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&family=Marcellus:wght@400&display=swap" rel="stylesheet">

    <!-- Vendor CSS Files -->
    <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
    <link href="assets/vendor/aos/aos.css" rel="stylesheet">
    <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">
    <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">

    <!-- Main CSS File -->
    <link href="assets/css/main.css" rel="stylesheet">

    <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
        }
    </style>

    <!-- =======================================================
    * Template Name: AgriCulture
    * Template URL: https://bootstrapmade.com/agriculture-bootstrap-website-template/
    * Updated: Aug 07 2024 with Bootstrap v5.3.3
    * Author: BootstrapMade.com
    * License: https://bootstrapmade.com/license/
    ======================================================== -->
</head>

<body>
  <body class="index-page">

  <header id="header" class="header d-flex align-items-center position-relative">
    <div class="container-fluid container-xl position-relative d-flex align-items-center justify-content-between">

      <a href="index.html" class="logo d-flex align-items-center">
        <img src="src/logo.png" alt="AgriCulture">
      </a>

      <nav id="navmenu" class="navmenu">
        <ul>
          <?php if (!isset($_SESSION['role'])): ?>
            <li><a href="index.php" class="active">Home</a></li>
            <li><a href="?page=about">About Us</a></li>
            <li><a href="?page=contact">Contact</a></li>
            <li><a href="login.php">Login</a></li>
          <?php else: ?>
            <?php if ($_SESSION['role'] == "Admin" || $_SESSION['role'] == "User"): ?>
              <li><a href="?page=service">Pembelajaran</a></li>
              <li class="dropdown"><a href="#"><span>Menu</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
                <ul>
                  <li><a href="#">Profil</a></li>
                  <li><a href="?page=contact">Contact</a></li>
                </ul>
              </li> <!-- Menambahkan tag penutup untuk li dropdown -->
            <?php endif; ?>
            <li><a href="logout.php">Log Out</a></li>
          <?php endif; ?>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>

    </div>
  </header>


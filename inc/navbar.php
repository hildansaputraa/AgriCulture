<body class="index-page">

  <header id="header" class="header d-flex align-items-center position-relative">
    <div class="container-fluid container-xl position-relative d-flex align-items-center justify-content-between">

      <a href="index.html" class="logo d-flex align-items-center">
        <!-- Uncomment the line below if you also wish to use an image logo -->
        <img src="src/logo.png" alt="AgriCulture">
        <!-- <h1 class="sitename">AgriCulture</h1>  -->
      </a>

      <nav id="navmenu" class="navmenu">
        <ul>
          <!-- Cek apakah pengguna sudah login -->
          <?php if (!isset($_SESSION['role'])): ?>
            <!-- Jika belum login, tampilkan menu Home, About Us, Contact -->
            <li><a href="index.php" class="active">Home</a></li>
            <li><a href="?page=about">About Us</a></li>
            <li><a href="?page=contact">Contact</a></li>
            <li><a href="login.php">Login</a></li>
          <?php else: ?>
            <!-- Jika sudah login, tampilkan menu sesuai role -->
             <?php if ($_SESSION['role'] == "Admin" || $_SESSION['role'] == "User"): ?>
              <li><a href="?page=service">Pembelajaran</a></li>
              <li class="dropdown"><a href="#"><span>Menu</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
            <ul>
            <li><a href="#">Profil</a></li>
            <li><a href="?page=contact">Contact</a></li>
            </ul>
            <?php endif; ?>
            <li><a href="logout.php">Log Out</a></li>
          <?php endif; ?>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>

    </div>
  </header>
</body>

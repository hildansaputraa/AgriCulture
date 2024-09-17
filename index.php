<?php


session_start();

// if (!isset($_SESSION['username'])) {
//   echo "<script> location.href='index.php' </script>";
// }


include "inc/header.php";
include "inc/navbar.php";
include "config/database.php";


if (isset($_GET['page'])) {
  $page = $_GET['page'];
  include "page/" . $page . ".php";
} else {
  include "page/dashboard.php";
}




include "inc/footer.php";

?>

 

  <!-- Scroll Top -->
  <a href="#" id="scroll-top" class="scroll-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <!-- Preloader -->
  <div id="preloader"></div>

  <!-- Vendor JS Files -->
  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/php-email-form/validate.js"></script>
  <script src="assets/vendor/aos/aos.js"></script>
  <script src="assets/vendor/swiper/swiper-bundle.min.js"></script>
  <script src="assets/vendor/glightbox/js/glightbox.min.js"></script>

  <!-- Main JS File -->
  <script src="assets/js/main.js"></script>

</body>

</html>
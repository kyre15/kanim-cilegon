var slideIndex = 1;

function setSubMenuOnLoad() {
    let selectedSubMenu = localStorage.getItem("subMenuSelected");

    document.getElementsByClassName("content-core-show")[0].className = "content-core-hide";
    document.getElementById(selectedSubMenu).classList.remove("content-core-hide");
    document.getElementById(selectedSubMenu).classList.add("content-core-show");
}

    function chartGenerator(id, sangatBaik, baik, kurangBaik, tidakBaik) {
          new Chart(document.getElementById('myChart'+id.toString()), {
            type: 'bar',
            data: {
              labels: ['P1'],
              datasets: [
                  {
                      label: 'Sangat Baik',
                      data: [sangatBaik],
                      borderWidth: 1
                  },
                  {
                      label: 'Baik',
                      data: [baik],
                      borderWidth: 1
                  },
                  {
                      label: 'Kurang Baik',
                      data: [kurangBaik],
                      borderWidth: 1
                  },
                  {
                      label: 'Tidak Baik',
                      data: [tidakBaik],
                      borderWidth: 1
                  },
              ]
            },
            options: {
              scales: {
                y: {
                  beginAtZero: true
                }
              }
            }
          });
    }

function showFirstSlide() {
    let slide = document.getElementsByClassName("mySlides")[0];
    slide.style.display = "block";
}

showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let items = document.getElementsByClassName("image-item");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < items.length; i++) {
    items[i].className = items[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
}

function dropdownLayanan() {
  document.getElementById("drop-layanan").classList.toggle("drop");
  document.getElementById("btnLayanan").classList.add('active');

  var getInformasiID = document.getElementById("drop-informasi");
  if (getInformasiID.className === "container-fluid-informasi drop") {
    getInformasiID.classList.remove('drop');
  }
  
  var getProfileID = document.getElementById("drop-profil");
  if (getProfileID.className === "container-fluid-profil drop") {
    getProfileID.classList.remove('drop');
  } 

  var getPPIDID = document.getElementById("drop-ppid");
  if (getPPIDID.className === "container-fluid-ppid drop") {
    getPPIDID.classList.remove('drop');
  } 
}

function dropdownInformasi() {
  document.getElementById("drop-informasi").classList.toggle("drop");
  document.getElementById("btnInformasi").classList.add('active');


  var getLayananID = document.getElementById("drop-layanan");
  if (getLayananID.className === "container-fluid-layanan drop") {
    getLayananID.classList.remove('drop');
  }
  
  var getProfileID = document.getElementById("drop-profil");
  if (getProfileID.className === "container-fluid-profil drop") {
    getProfileID.classList.remove('drop');
  } 

  var getPPIDID = document.getElementById("drop-ppid");
  if (getPPIDID.className === "container-fluid-ppid drop") {
    getPPIDID.classList.remove('drop');
  } 
}

function dropdownProfil() {
  document.getElementById("drop-profil").classList.toggle("drop");
  document.getElementById("btnProfil").classList.add('active');


  var getInformasiID = document.getElementById("drop-informasi");
  if (getInformasiID.className === "container-fluid-informasi drop") {
    getInformasiID.classList.remove('drop');
  }
  
  var getLayananID = document.getElementById("drop-layanan");
  if (getLayananID.className === "container-fluid-layanan drop") {
    getLayananID.classList.remove('drop');
  }

  var getPPIDID = document.getElementById("drop-ppid");
  if (getPPIDID.className === "container-fluid-ppid drop") {
    getPPIDID.classList.remove('drop');
  } 
}

function dropdownPPID() {
  document.getElementById("drop-ppid").classList.toggle("drop");
  document.getElementById("btnPPID").classList.add('active');

  var getInformasiID = document.getElementById("drop-informasi");
  if (getInformasiID.className === "container-fluid-informasi drop") {
    getInformasiID.classList.remove('drop');
  }
  
  var getProfileID = document.getElementById("drop-profil");
  if (getProfileID.className === "container-fluid-profil drop") {
    getProfileID.classList.remove('drop');
  } 

  var getLayananID = document.getElementById("drop-layanan");
  if (getLayananID.className === "container-fluid-layanan drop") {
    getLayananID.classList.remove('drop');
  }
}

function overlayOn() {
  const popup = document.querySelector(".full-screen");
  popup.classList.remove('hidden');
}

function overlayMaklumatOff() {
    const popup = document.querySelector(".overlay");
    popup.classList.add("hidden");
}
function overlayOff() {
  const popup = document.querySelector(".full-screen");
  popup.classList.add("hidden");
    
  document.getElementById("btnLayanan").classList.remove('active');
  document.getElementById("btnInformasi").classList.remove('active');
  document.getElementById("btnProfil").classList.remove('active');
  document.getElementById("btnPPID").classList.remove('active');

  var getInformasiID = document.getElementById("drop-informasi");
  if (getInformasiID.className === "container-fluid-informasi drop") {
    getInformasiID.classList.remove('drop');
  }
  
  var getProfileID = document.getElementById("drop-profil");
  if (getProfileID.className === "container-fluid-profil drop") {
    getProfileID.classList.remove('drop');
  } 

  var getLayananID = document.getElementById("drop-layanan");
  if (getLayananID.className === "container-fluid-layanan drop") {
    getLayananID.classList.remove('drop');
  }
    
  var getPPIDID = document.getElementById("drop-ppid");
  if (getPPIDID.className === "container-fluid-ppid drop") {
    getPPIDID.classList.remove('drop');
  } 
}

const nav = document.getElementById('mytopnav');
window.addEventListener("scroll", function(){
  if(document.documentElement.scrollTop > 20) {
    nav.classList.add("sticky");
  } else {
    nav.classList.remove("sticky");
  }
})

// function dropdownItemChecker() {  for adjusting dropdown height **
//     var getWNIid = document.querySelectorAll('.header-menu-items.header-menu-item').length;
//     var getWNAid = document.querySelectorAll('.header-menu-items.header-menu-item').length;
//     let getStyle = document.getElementsByClassName('.dropdown-header.container-fluid').

//     if (getWNIid.length == 5) {
//       getStyle.height(252);
//     } else if (getWNIid.length == 4) {
//       getStyle.height(222);
//     } else if (getWNIid.length == 3) {
//       getStyle.height(202);
//     } else if (getWNIid.length == 2) {
//       getStyle.height(182);
//     } else if (getWNIid.length == 1) {
//       getStyle.height(162);
//     }
//   }

function autoScroll(element) {
    document.getElementById(element).scrollIntoView();
}

function changeSubMenuTab(buttonClicked) {

    var els = Array.prototype.slice.call( document.getElementsByClassName(buttonClicked.className), 0 );
    var indexElement = els.indexOf(event.currentTarget)
    // alert(els.indexOf(event.currentTarget))

    var a = document.getElementsByClassName('tentang-layanan-dan-persyaratan-content')[indexElement]
    var b = document.getElementsByClassName('alur-proses-dan-prosedur-content')[indexElement]
    var c = document.getElementsByClassName('biaya-button-content')[indexElement]

    switch (buttonClicked.className) {
        case 'tentang-layanan-dan-persyaratan-button':
                a.style.display = "flex"
                b.style.display = "none"
                c.style.display = "none"
            break;
        case 'alur-proses-dan-prosedur-button':
                a.style.display = "none"
                b.style.display = "flex"
                c.style.display = "none"
            break;
        case 'biaya-button':
                a.style.display = "none"
                b.style.display = "none"
                c.style.display = "flex"
            break
    }
}

function changeSubMenu(clickedSubMenu) {
    document.getElementsByClassName("content-core-show")[0].className = "content-core-hide";
    document.getElementById(clickedSubMenu).classList.remove("content-core-hide");
    document.getElementById(clickedSubMenu).classList.add("content-core-show");
}

function selectSubMenu(clickedSubMenu) {
    localStorage.setItem("subMenuSelected", clickedSubMenu);
}

function shortCutTab(shortcut) {
    var wni = document.getElementsByClassName('shortcut-item-container-wni')[0];
    var wna = document.getElementsByClassName('shortcut-item-container-wna')[0];

    switch (shortcut) {
    case 'wni':
        wni.style.display = "inline-block";
        wna.style.display = "none";
        break;
    case 'wna':
        wni.style.display = "none";
        wna.style.display = "inline-block";
        break;
    }
}

function galeri(tab){
  var fotoTabElement = document.getElementsByClassName('galeri-foto-grid-wrapper')[0];
  var videoTabElement = document.getElementsByClassName('galeri-video-grid-wrapper')[0];

  switch (tab) {
    case 'foto':
        fotoTabElement.style.display = "flex";
        videoTabElement.style.display = "none";
        break;
    case 'video':
        fotoTabElement.style.display = "none";
        videoTabElement.style.display = "flex";
        break;
    }
}

function dasbor(tab){
  var laporanTabElement = document.getElementsByClassName('rinci-pelayanan-container')[0];
  var ipkdanikmTabElement = document.getElementsByClassName('ipk-dan-ikm-container')[0];

  switch (tab) {
    case 'laporan':
        laporanTabElement.style.display = "flex";
        ipkdanikmTabElement.style.display = "none";
        break;
    case 'ipkdanikm':
        laporanTabElement.style.display = "none";
        ipkdanikmTabElement.style.display = "flex";
        break;
    }
}

function berita(tab) {
    var kantorImigrasiCilegonEle = document.getElementsByClassName('berita-grid-kantor-imigrasi-cilegon')[0];
    var kemenkumhamRepublikIndonesiaEle = document.getElementsByClassName('berita-grid-kemenkumham-republik-indonesia')[0];
    var kemenkumhamKanwilBantenEle = document.getElementsByClassName('berita-grid-kemenkumham-kanwil-banten')[0];

    var kantorImigrasiCilegonHeader = document.getElementById('kantor_imigrasi_cilegon_header')
    var kemenkumhamRepublikIndonesiaHeader = document.getElementById('kemenkumham_republik_indonesia_header')
    var kemenkumhamKanwilBanten = document.getElementById('kemenkumham_kanwil_banten_header')

    switch (tab) {
        case 'kantor-imigrasi-cilegon':
            kantorImigrasiCilegonEle.style.display = "flex";
            kemenkumhamRepublikIndonesiaEle.style.display = "none";
            kemenkumhamKanwilBantenEle.style.display = "none";
            kantorImigrasiCilegonHeader.classList.remove("hide");
            kantorImigrasiCilegonHeader.classList.add("show");
            kemenkumhamRepublikIndonesiaHeader.classList.add("hide");
            kemenkumhamKanwilBanten.classList.add("hide");
            break;
        case 'kemenkumham-republik-indonesia':
            kantorImigrasiCilegonEle.style.display = "none";
            kemenkumhamRepublikIndonesiaEle.style.display = "flex";
            kemenkumhamKanwilBantenEle.style.display = "none";
            kantorImigrasiCilegonHeader.classList.add("hide");
            kemenkumhamRepublikIndonesiaHeader.classList.remove("hide");
            kemenkumhamRepublikIndonesiaHeader.classList.add("show");
            kemenkumhamKanwilBanten.classList.add("hide");
            break;
        case 'kemenkumham-kanwil-banten':
            kantorImigrasiCilegonEle.style.display = "none";
            kemenkumhamRepublikIndonesiaEle.style.display = "none";
            kemenkumhamKanwilBantenEle.style.display = "flex";
            kantorImigrasiCilegonHeader.classList.add("hide");
            kemenkumhamRepublikIndonesiaHeader.classList.add("hide");
            kemenkumhamKanwilBanten.classList.remove("hide");
            kemenkumhamKanwilBanten.classList.add("show");
            break;
    }
}

function dropDownPelayanan() {
    var selectBox = document.getElementById("laporan-dropdown");
    var selectedValue = selectBox.options[selectBox.selectedIndex].value;

    let bulanIniDropdown = document.getElementsByClassName('laporan-bulan-ini')[0];
    let tahunIniDropdown = document.getElementsByClassName('laporan-tahun-ini')[0];
    let mingguIniDropdown = document.getElementsByClassName('laporan-minggu-ini')[0];

    switch (selectedValue) {
        case 'bulan-ini':
            bulanIniDropdown.style.display = "flex";
            tahunIniDropdown.style.display = "none";
            mingguIniDropdown.style.display = "none";
            break;
        case 'tahun-ini':
            bulanIniDropdown.style.display = "none";
            tahunIniDropdown.style.display = "flex";
            mingguIniDropdown.style.display = "none";
            break;
        case 'minggu-ini':
            bulanIniDropdown.style.display = "none";
            tahunIniDropdown.style.display = "none";
            mingguIniDropdown.style.display = "flex";
            break;
    }
}

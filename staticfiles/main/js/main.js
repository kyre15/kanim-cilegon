function navbarResponsive() {
  var x = document.getElementById("mytopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}
function galeri(tab) {
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

function berita(tab) {
    var kantorImigrasiCilegonEle = document.getElementsByClassName('berita-grid-kantor-imigrasi-cilegon')[0];
    var kemenkumhamRepublikIndonesiaEle = document.getElementsByClassName('berita-grid-kemenkumham-republik-indonesia')[0];
    var kemenkumhamKanwilBantenEle = document.getElementsByClassName('berita-grid-kemenkumham-kanwil-banten')[0];

    switch (tab) {
        case 'kantor-imigrasi-cilegon':
            kantorImigrasiCilegonEle.style.display = "flex";
            kemenkumhamRepublikIndonesiaEle.style.display = "none";
            kemenkumhamKanwilBantenEle.style.display = "none";
            break;
        case 'kemenkumham-republik-indonesia':
            kantorImigrasiCilegonEle.style.display = "none";
            kemenkumhamRepublikIndonesiaEle.style.display = "flex";
            kemenkumhamKanwilBantenEle.style.display = "none";
            break;
        case 'kemenkumham-kanwil-banten':
            kantorImigrasiCilegonEle.style.display = "none";
            kemenkumhamRepublikIndonesiaEle.style.display = "none";
            kemenkumhamKanwilBantenEle.style.display = "flex";
            break;
    }
}


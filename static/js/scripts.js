/*!
    * Start Bootstrap - SB Admin v7.0.7 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2023 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});


var button = document.getElementById("btnNavbarSearch");

button.addEventListener("click", function() {
    // 얼럿 띄우기
    alert("검색기능 준비중");
});


var link = document.getElementById("albumtag");

// 링크 클릭 이벤트 핸들러를 추가
link.addEventListener("click", function(event) {
    // 기본 동작 (페이지 이동)을 막음
    event.preventDefault();

    // 얼럿 띄우기
    alert("앨범 기능 준비중");
});
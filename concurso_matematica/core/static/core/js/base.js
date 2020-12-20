"use strict";

//CONSTANTS
const nav = document.querySelector('.nav');
const navList = document.querySelector('.nav-list');
const menuButton = document.getElementById('menu-button');
const closeDropDivButton = document.getElementById('close-dropdiv-button');
const searchButton = document.getElementById('search-button');
const searchFieldCancel = document.getElementById("search-field-cancel");
const searchFieldGroup = document.getElementById('search-field-group');
const searchFieldInput = searchFieldGroup.children[0];
const bgArrow = document.querySelector('#site-bg button');
const mainNav = document.getElementById('main-nav');
var scrollPos = 0;




//EVENT HANDLERS
var dropMenu = (e) => {
    if(navList.style.display != "flex"){
        navList.style.display = "flex";
        navList.style.top = "0";
     
    }
    else {
        
        navList.style.top = "-100vh";
        setTimeout(()=>{
            navList.style.display = "none";
        }, 500);
        
    }
    
    //let length = navList.children.length;

}

var dropSearchField = (e) => {
    if(searchFieldGroup.style.display != "flex"){
       
        searchFieldGroup.style.display = "flex";
        searchFieldGroup.style.bottom = "-160px";
    }else{
        searchFieldGroup.style.bottom = "-100px";
        setTimeout(()=>{
          searchFieldGroup.style.display = "none";  
        },500);
    }
    
    
};

var searchFieldInputQuery = (e) => {
    if(e.keyCode == 13){
        alert('En implementacion!!');
    }
};

var scrollToSiteMenuBar = (e) => {
    if(window.scrollY >= 0 || windows.scrollY < window.innerHeight){
        document.documentElement.scrollTop = window.innerHeight;
        
        
        
    }
};

function dropMainNav(evt){
    scrollPos = document.body.scrollTop;
    if(document.body.scrollTop >= mainNav.offsetHeight){

    } 
}

//EVENT LISTENERS
menuButton.addEventListener('click', dropMenu);
closeDropDivButton.addEventListener('click', dropMenu);
searchFieldCancel.addEventListener('click', dropSearchField);
searchButton.addEventListener('click', dropSearchField);
searchFieldInput.addEventListener('keydown', searchFieldInputQuery);
bgArrow.addEventListener('click', scrollToSiteMenuBar);
/*navList.addEventListener('transitionend', ()=>{
    navList.style.display = "none";
});*/
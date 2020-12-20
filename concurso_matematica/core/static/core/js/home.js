var texts = document.getElementsByClassName('card-text');
var readMoreButton = document.getElementsByClassName('read-more');
var userMenu = document.getElementById('user-menu');
var userMenuButton = document.getElementsByClassName('user-menu-toggler')[0];

let expression = /\d+/;

let count = 0;
for (let x of texts) {
  console.log(x);
  $clamp(x, { clamp: 4, animate: true });
}

/*for (let x = 0; x < texts.length; x++) {

  if (Math.ceil(expression.exec(getComputedStyle(texts[x], null).height) / expression.exec(getComputedStyle(texts[x], null).lineHeight)) >= 4) {
    readMoreButton[x].classList.replace('d-none', 'd-inline-block');
  }

}*/

function isChildOfParent(child, ancestor){
  let childParent = child.parentNode;
  while(childParent != null){
    if(childParent === ancestor)
      return true
    childParent = childParent.parentNode;
  }
  return false
}

function showUserMenu(evt) {
 
}

userMenuButton.addEventListener('click', showUserMenu);
userMenu.addEventListener('focusout', showUserMenu);

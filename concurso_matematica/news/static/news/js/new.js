function showCommentBox(event){
    let mainComment = getMainComment(event.target);
    let subCommentBox = mainComment.querySelector('.user-subcomment');
    subCommentBox.classList.remove('hidden');
    
}

function getMainComment(child){

    if (child.classList.contains('maincomment')) {
        return child;
    } else {
        if(child === document.body)
            return false
        return getMainComment(child.parentElement);
    }
}
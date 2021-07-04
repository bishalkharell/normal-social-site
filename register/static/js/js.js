
const dropbtn = document.querySelector(".user-model-info");
const dropMenu = document.querySelector(".dropdown-menu");
const dropDownnPic = document.querySelector(".user-model-info i");
const bodyContainer = document.querySelector(".bodyContainer");


state = false;
dropbtn.addEventListener('click',showMenu);


function showMenu(){
    if(!state){
    dropMenu.style.transform="scale(1,1)";
    dropMenu.style.transformOrigin="top";
    dropMenu.style.transition="0.3s ease-in-out";
    dropDownnPic.style.transform="rotate(180deg)";
    dropDownnPic.style.transition="0.3s ease-in";

    state = true;
    }else{
        dropMenu.style.transform="scale(0,0)";
        dropMenu.style.transition="0.3s ease-in-out";
        dropDownnPic.style.transform="rotate(-360deg)";
        dropDownnPic.style.transition="0.3s ease-in";


        state = false;
    }

}




// function delete_account(){
//     var delete_info = document.getElementById('delete-info')
//     // delete_info.style.transform="scale(1,1)"
//     // delete_info.style.transformOrigin="left";
//     // delete_info.style.transition =" 500ms ease";

// }



function show_addBlog(){
    let blog = document.getElementById('addBlog');
    blog.style.position="static";
    blog.style.transform="scale(1,1)";
    // blog.style.transition = "500ms ease";
    
}


function hide_modal(){
    var delete_info = document.getElementById('delete-info')
    delete_info.style.transform="scale(0,0)"
    delete_info.style.transformOrigin="left";
    delete_info.style.transition =" 500ms ease"
}



function checkImage(){
        let imageContainer = document.querySelector('.gallery_container');
        let allImage = document.querySelectorAll('.gallery_container img');

        try{
        if(allImage.length <= 2){
            imageContainer.style.gridTemplateColumns = " repeat(auto-fit, minmax(100px,100px))";
        };
        }catch(err){
            console.log("Typecatch error");
    }
        
}
checkImage();






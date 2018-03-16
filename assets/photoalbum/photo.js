import $ from 'jquery'

$(document).ready(() => {
  console.log("Running second script")
  
  $(".photo .big").bind("keydown", function(e) {
    if (e.keyCode == 37) { // Left
      console.log("Left arrow")
    }
    if (e.keyCode == 39) { // Right arrow
      console.log("Right arrow")
    }
  })


  $(document).keypress(function(event) {
    console.log("Event!");
    if (event == 37) {
        console.log("Left pointer");
        var previousPhotoUrl = $(this).getElementById('previous_photo_url').href;
        window.location.replace(previousPhotoUrl);

    } else if (event == 39) {
      console.log("Right pointer");

    }

  })
})
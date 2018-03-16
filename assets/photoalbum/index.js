import $ from 'jquery'

import './less/photoalbum.less'

$(document).ready(() => {
  console.log('Running the script')
  $('.photo_edit').click(function choose_photo (e) {
		const photo = $(this)
		photo.toggleClass('chosen')
  })

  $('#show_report_photo_form').click(function show_form (e) {
		console.log("Changing visibility")
		const button = $(this)
		//button.style["visibility"] = "hidden"
		document.getElementById('show_report_photo_form').style["visibility"] = "hidden"
		document.getElementById('report_photo_form').style["visibility"] = "visible"
  })

  $(document).keydown(function(event) {
    if (event.key == "ArrowLeft") {
        var previousPhotoUrl = document.getElementById('previous_photo_url').href;
        window.location.replace(previousPhotoUrl);
    } else if (event.key == "ArrowRight") {
      var nextPhotoUrl = document.getElementById('next_photo_url').href;
      window.location.replace(nextPhotoUrl);
    }
  })

})






function PreviewImage()
    {
        let imgid = event.srcElement.id.substring(8,9);
        let oFReader = new FileReader();
        oFReader.readAsDataURL(document.getElementById(event.srcElement.id).files[0]);

        oFReader.onload = function (oFREvent) {
            document.getElementById(imgid).src = oFREvent.target.result;
        }
    };

// document.addEventListener('mouseover', (e) => {
//     if (e.target.id == '1' || e.target.id == '2' || e.target.id == '3' || e.target.id == '4')
//     {
//         document.getElementById('0').src = document.getElementById(e.target.id).src;
//     }
// })

// <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
//
// $("#0").click(function () {
//     $("#id_form-0-img").trigger('click');
// });

// function GFG_Fun() {
//                 document.getElementById('file').parentNode.removeChild(document.getElementById('0'));
//             }
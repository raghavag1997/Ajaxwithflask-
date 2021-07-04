$(document).ready(function (e) {
    $('#upload').on('click', function () {
        var form_data = new FormData();

        //Getting File Name 
            //var filename=document.getElementById('myfile').files[0].name;
        
        // Appending Form data into one key myfile
        form_data.append('mydata',document.getElementById('myfile').files[0])

        //Printing Form Data values
            // for (var value of form_data.values()) {
            //     console.log(value);
            //  }
        
            $.ajax({
                url: 'python-flask-files-upload', // point to server-side URL
                dataType: 'json', // what to expect back from server
                cache: false,
                contentType: false,
                processData: false,
                data: form_data,
                type: 'post',
                success: function (response) { // display success response
                    console.log(response.message)
                    document.getElementById('msg').innerHTML=response.message;
                    // alert('File Upload Sucessfully');
                },
                error: function (response) {
                    document.getElementById('msg').innerHTML=response.responseJSON.filetype;
                    console.log(response.responseJSON.filetype)
                    //var str=JSON.stringify(response)
                    //console.log(str)
                    //alert('File Not Upload Sucessfully');
                    //alert(response.); // display error response
                }
            });
        
    });
});
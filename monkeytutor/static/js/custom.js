

let autocomplete;

function initAutoComplete(){
autocomplete = new google.maps.places.Autocomplete(
    document.getElementById('id_address'),
    {
        types: ['geocode', 'establishment'],
        //default in this app is "SG" - add your country code
        componentRestrictions: {'country': ['SG']},
    })
// function to specify what should happen when the prediction is clicked
autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged (){
    var place = autocomplete.getPlace();

    // User did not select the prediction. Reset the input field or alert()
    if (!place.geometry){
        document.getElementById('id_address').placeholder = "Start typing...";
    }
    else{
        console.log('place name=>', place.name)
    }
    // get the address components and assign them to the fields
    var geocoder= new google.maps.Geocoder()
    var address = document.getElementById('id_address').value
    geocoder.geocode({'address':address},function(results,status){
        if(status==google.maps.GeocoderStatus.OK){
            var latitude = results[0].geometry.location.lat();
            var longitude = results[0].geometry.location.lng();
            $('#id_longitude').val(longitude)
            $('#id_latitude').val(latitude)
            $('#id_address').val(address)
        }
    });
    for(var i=0; i<place.address_components.length; i++){
        for(var j=0; j<place.address_components[i].types.length; j++){
            if(place.address_components[i].types[j]=="postal_code"){
                $('#id_zip_code').val(place.address_components[i].long_name)
            }
            
        }
        
    }
}



$(document).ready(function(){

    // only show subjects based on whether primary or secondary is selected
    // start
    // set all values to hidden except primary subjects
    try {
        values = document.querySelectorAll(`[id^="id_subjects"]`);
        let elements = Array.from(values)
        for (let x = 0; x < elements.length; x++) {
            search = $(elements[x]).attr('id')
            y = document.querySelector("label[for=" + search+ "]");
            content = y.textContent.toLowerCase()
            if (content.includes('primary')) { // sets the div of input tags that contain the word primary to block, else make them hidden
                elements[x].parentElement.style.display = 'block'
            }else{
                elements[x].parentElement.style.display = 'none'
            }
        }
      }
      catch(err) {
        console.log('Not in Registration page')
      }
    // toggle hidden and block based on whether primary and secondary are selected
    $( ".select_type" ).click(function() {
        
        
        values = document.querySelectorAll(`[id^="id_subjects"]`);
        let elements = Array.from(values)
        console.log(elements.constructor)
        for (let j = 0; j < elements.length; j++) {
            search = $(elements[j]).attr('id') // get the id of the input element
            x = document.querySelector("label[for=" + search+ "]"); // get label tag based on id since they share the same id
            content = x.textContent.toLowerCase() // set both to lowercase
            if (content.includes(this.id.toLowerCase())) { // check whether value of label contains primary/secondary/JC depending on which is selected
                elements[j].parentElement.style.display = 'block'
            }else{
                elements[j].parentElement.style.display = 'none'
            }
        }
       
    // end 

        
        
      });

  });


  $(document).ready(function(){
    $('.delete_assignment').on('click',function(e){
        e.preventDefault()
        assignment_id = $(this).attr('data-id');
        url = $(this).attr('data-url');
        data = {
            assignment_id: assignment_id,
        }
        $.ajax({
            type: 'GET',
            url: url,
            data:data,
            success: function(response){
                console.log('Assignment ' + response.assignment + " has been deleted")
                if(response.status=="SUCCESS"){
                    document.getElementById(assignment_id).remove()
                }

            }
            
        })
    })
})



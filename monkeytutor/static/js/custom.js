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
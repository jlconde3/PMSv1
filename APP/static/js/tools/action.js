let j = 1;

document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools");
});

document.getElementById('more_button').addEventListener('click',() => {
    let i = j;
    console.log("Hola")

    add_more('subactions',
    `
    <div>
        <label class = "label-title">Subaction</label>
    </div>
    <div class="fields-group">
        <div>
            <label class = "label-field">Custom code</label><br>
            <input name="custom_code" class = "input-4" type="text">
        </div>
        <div class="dropdwn">
            <label class = "label-field">Zone</label><br>
            <input name = "subaction_zone" class = "input-4" type="text"  id = "zone_${j}">
            <datalist id="zones_${j}" class = "input-4"></datalist>
        </div>
        <div class="dropdwn">
            <label class = "label-field">Area</label><br> 
            <input name="subaction_area" id = "area_${j}" class = "input-4" type="text">
            <datalist id="areas_${j}" class = "input-4" ></datalist>
        </div>
        <div>
            <label class = "label-field">Time</label><br>
            <input name = "subaction_time" class = "input-4" type="number">
        </div>
    </div>
    `);
    j++;
});

document.getElementById('action_description').addEventListener('keyup',()=>{
    var characterCount = document.getElementById('action_description').value.length;
    current = document.getElementById('current');
    current.innerText = characterCount;

});
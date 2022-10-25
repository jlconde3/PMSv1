//Var for actions id numbers
let n = 1;

//Template for actions
let action_template = `
    <div>
        <label class = "label-title">Subaction</label>
    </div>
    <div class="fields-group">
        <div>
            <label class = "label-field">Code</label><br>
            <input class = "input-4" id = "internal_code">
        </div>
        <div>
            <label class = "label-field">Zone</label><br>
            <input class = "input-4" id = "zone_code">
        </div>
        <div>
            <label class = "label-field">Area</label><br>
            <input class = "input-4" type="text" id = "area_code">
        </div>
        <div>
            <label class = "label-field">Time</label><br>
            <input class = "input-4" type="number" id = "time">
        </div>
    </div>
`

document.getElementById('more_button').addEventListener('click',() => 
    add_more( 'subactions',`action_${n}`,action_template)
);

document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools")
});




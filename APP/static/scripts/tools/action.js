//Var for actions id numbers
let n = 1;

//Template for actions
let action_template = `
    <div>
        <label class = "label-title">Subaction</label>
        </div>
        <div class="fields-group">
        <div>
            <label class = "label-field">Custom code</label><br>
            <input class = "input-4" type="text" name = "custom_code">
        </div>
        <div>
            <label class = "label-field">Zone</label><br>
            <input class = "input-4" type="text" name = "subaction_zone">
        </div>
        <div>
            <label class = "label-field">Area</label><br>
            <input class = "input-4" type="text" name = "subaction_area">
        </div>
        <div>
            <label class = "label-field">Time</label><br>
            <input class = "input-4" type="number" name = "subaction_time">
        </div>
    </div>
`

document.getElementById('more_button').addEventListener('click',() => 
    add_more( 'subactions',`subaction_${n}`,action_template)
);

document.getElementById('submit_button').addEventListener('click',() => {
    let data = {
        project_code: element_id_value('project_code'),
        action_customer_code: element_id_value('customer_code'),
        action_type_code: element_id_value('action_type'),
        action_date: element_id_value('action_date'),
        action_discipline_code: element_id_value('discipline_code'),
        action_phase_code: element_id_value('phase_code'),
        action_phase_code: element_id_value('action_description'),
        custom_code: element_name_value('custom_code'),
        subaction_zone: element_name_value('subaction_zone'),
        subaction_area: element_name_value('subaction_area'),
        subaction_time: element_name_value('subaction_time')
    }

    fetch('/tools/create_action', {
        credentials: 'include',
        method: 'POST',
        body: JSON.stringify(data),
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(window.location.replace("/tools"))

});

document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools")
});




document.getElementById('cancel_button').addEventListener('click',() => {
    window.location.replace("/tools");
});

document.getElementById('retrive_button').addEventListener('click',function retrive_data(){
    const code = document.getElementById('code').value 
    if (code == ""){
        window.alert("Hola")
    }

    fetch('/projects/retrive_data',{
        credentials: 'include',
        method: 'POST',
        body: JSON.stringify({code:code}),
        headers:{'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(data => console.log(data['response']))
});

document.getElementById('reload_button').addEventListener('click',function reload_hours(){
    const budget = document.getElementsByName('budget');
    const margin = document.getElementsByName('margin');
    const cpt = document.getElementsByName('default');
    const management = document.getElementsByName('management');
    const other = document.getElementsByName('others');
    const usefull_hours = budget[0].value*(1-margin[0].value);
    const management_hours = usefull_hours*management[0].value;
    const other_hours = usefull_hours*other[0].value;

    document.getElementById('work_result').value = (usefull_hours-management_hours-other_hours)/cpt[0].value
    document.getElementById('management_result').value = management_hours/cpt[0].value
    document.getElementById('other_result').value = other_hours/cpt[0].value

});


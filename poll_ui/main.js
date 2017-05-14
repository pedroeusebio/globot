$(document).ready(function() {
  $('.alert-success').hide();
  $('.alert-danger').hide();
});

$("#createPoll").submit(function(e) {
  e.preventDefault();
  var payload = submitPoll(this);
  var payload = {
    question: $(".js-question").val(),
    team: $(".js-time").val(),
    options: $(".js-option").map((i,x) => $(x).val()).toArray()
  }
  $.ajax({
    method: 'POST',
    url: '/createPoll/',
    contentType: 'application/json',
    data: JSON.stringify(payload)
  })
});

function submitPoll(p) {
  var poll = $(p);
  var serial = poll.serializeArray();
  var obj = {option: []};
  serial.map(function(e) {
    if (e.name == 'option'){
      obj.option.push(e.value);
    } else {
      obj[e.name] = e.value;
    }
  });
  return obj;
}

$('#addOption').on('click', function() {
  var numOption = $('.input-group').length;
  var $option = $(`<div class="col-sm-8 input-group"><span class="input-group-addon">Opcao ${numOption}</span><input type="text" class="js-option form-control" placeholder="opcao" aria-describedby="sizing-addon2"></div>`);
  $('#div-options').append($option);
});

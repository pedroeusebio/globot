$(document).ready(function() {

  $('#addOption').on('click', function() {
    var numOption = $('#div-options .input-group').length + 1;
    var $option = $(`<div class="col-sm-8 input-group"><span class="input-group-addon">Opcao ${numOption}</span><input type="text" class="js-option form-control" placeholder="opcao" aria-describedby="sizing-addon2"></div>`);
    $('#div-options').append($option);
  });

  $('#alternate').on('click', function() {
    if ($('.wrapper-create').is(':hidden')) {
      $('.wrapper-create').show();
      $('.wrapper-list').hide();
      $(this).prop('value', 'Cancelar Enquete');
      $(this).removeClass('btn-info').addClass('btn-danger');
    } else {
      $('.wrapper-create').hide();
      $('.wrapper-list').show();
      $('#createPoll').trigger('reset');
      $(this).prop('value', 'Criar Enquete');
      $(this).removeClass('btn-danger').addClass('btn-info');
    }
  });
  window.setInterval(updatePolls, 10000);
  updatePolls();
});

function updatePolls(){
  $.getJSON("/polls").then((polls) => {
    $('.wrapper-list').html(polls.map(renderPoll).reduce((a,b) => a + b));
  });
}

$("#createPoll").submit(function(e) {
  e.preventDefault();
  var payload = {
    question: $(".js-question").val(),
    team: $(".js-time").val(),
    options: $(".js-option").map((i,x) => $(x).val()).toArray()
  };
  $.ajax({
    method: 'POST',
    url: '/createPoll/',
    contentType: 'application/json',
    data: JSON.stringify(payload)
  }).then(updatePolls);
});

function renderPoll(poll){
  var totalVotes = poll.options.map((x) => poll.results[x]).reduce((a,b) => a+b);
  var percent = (opt) => poll.results[opt]*100/totalVotes;
  var options = poll.options.map((opt) => `
    <div class="option">
      <label class="option-label" name="option-label">${opt}</label>
      <div class="progress">
        <div class="progress-bar" role="progressbar" aria-valuenow="${percent(opt)}" aria-valuemin="0" aria-valuemax="100" style="width: ${percent(opt)}%;"></div>
      </div>
    </div>
  `);
  var html = `
    <div class="poll">
      <div class="row">
        <div class="question">
          <div class="col-sm-8">
            <label for="question-show">Pergunta </label>
            <span class="" name="question-show">${poll.question}</span>
          </div>
        </div>
        <div class="col-sm-8">
          <div class="options">
            ${options.reduce((a,b) => a+b)}
          </div>
        </div>
      </div>
    </div>
  `;
  return html;
}

window.onload = function() {
  $('.basket-list').on('click', 'input[type="number"]', function() {
    var targetHref = event.target;
    console.log(targetHref);
  });
}
 // Disable +/- buttons outside 1-99 range
 function handleEnableDisable(itemId) {
   const currentValue = parseInt($(`.id_qty_${itemId}`).val());
   const minusDisabled = currentValue <= 0;
   const plusDisabled = currentValue >= 1;
   $(`.decrement-qty_${itemId}`).prop('disabled', minusDisabled);
   $(`.increment-qty_${itemId}`).prop('disabled', plusDisabled);
 }

 // Ensure proper enabling/disabling of all inputs on page load
 const allQtyInputs = $('.qty_input');
 for (let i = 0; i < allQtyInputs.length; i++) {
   const itemId = $(allQtyInputs[i]).data('item_id');
   handleEnableDisable(itemId);
 }

 // Check enable/disable every time the input is changed
 $('.qty_input').change(function () {
   const itemId = $(this).data('item_id');
   handleEnableDisable(itemId);
 });

 // Increment quantity
 $('.increment-qty').click(function (e) {
   e.preventDefault();
   const itemId = $(this).data('item_id');
   const closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   const allInputs = $(`.input-group-${itemId} input`);
   const currentValue = parseInt($(closestInput).val());
   $(allInputs).val(currentValue + 1);
   handleEnableDisable(itemId);
 });

 // Decrement quantity
 $('.decrement-qty').click(function (e) {
   e.preventDefault();
   const itemId = $(this).data('item_id');
   const closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   const allInputs = $(`.input-group-${itemId} input`);
   const currentValue = parseInt($(closestInput).val());
   $(allInputs).val(currentValue - 1);
   handleEnableDisable(itemId);
 });
const productsGroup = document.querySelector('.products-group');
const productGroupButton = document.querySelector('.calculate-form-group-button');
const productDelete = document.querySelector('.product-group-delete');
const products = [];

productGroupButton.addEventListener('click', saveItems);

function saveItems() {
   const productsGroupItem = document.querySelectorAll('.products-group .products-group-item');
   const productsGroupItemLast = productsGroupItem[productsGroupItem.length - 1];

   const name = productsGroupItemLast.querySelector('.product-group-name input').value;
   const weight = productsGroupItemLast.querySelectorAll('.product-group-properties__item input')[0].value;
   const len = productsGroupItemLast.querySelectorAll('.product-group-properties__item input')[1].value;
   const width = productsGroupItemLast.querySelectorAll('.product-group-properties__item input')[2].value;
   const height = productsGroupItemLast.querySelectorAll('.product-group-properties__item input')[3].value;

   if (
      name.length &&
      weight.length &&
      len.length &&
      width.length &&
      height.length
   ) {
      products.push({
         name,
         weight: Number(weight),
         len: Number(len),
         width: Number(width),
         height: Number(height)
      });

      renderProductsItem();
   }
}

function deleteItem(idx) {
   products.splice(idx, 1);
   renderProductsItem()
}

function renderProductsItem() {
   let content = '';

   products.forEach((product, idx) => {
      content += `
         <div class="products-group-item">
            <div class="product-group-name">
               <div class="product-group-name-header">
                  <label>Название</label>
                  <p uk-tooltip="title: Удалить; pos: left" onClick="deleteItem(${idx})">
                     <span uk-icon="minus-circle"></span>
                  </p>
               </div>
               <input type="text" value="${product.name}">
            </div>
      
            <div class="product-group-properties">
               <div class="product-group-properties__item">
                  <label>Вес</label>
                  <input type="text" value="${product.weight}">
               </div>
               <div class="product-group-properties__item">
                  <label>Длина</label>
                  <input type="text" value="${product.len}">
               </div>
               <div class="product-group-properties__item">
                  <label>Ширина</label>
                  <input type="text" value="${product.width}">
               </div>
               <div class="product-group-properties__item">
                  <label>Высота</label>
                  <input type="text" value="${product.height}">
               </div>
            </div>
         </div>
      `;
   });

   content += `
      <div class="products-group-item">
         <div class="product-group-name">
            <div class="product-group-name-header">
               <label>Название</label>
            </div>
            <input type="text">
         </div>

         <div class="product-group-properties">
            <div class="product-group-properties__item">
               <label>Вес</label>
               <input type="text">
            </div>
            <div class="product-group-properties__item">
               <label>Длина</label>
               <input type="text">
            </div>
            <div class="product-group-properties__item">
               <label>Ширина</label>
               <input type="text">
            </div>
            <div class="product-group-properties__item">
               <label>Высота</label>
               <input type="text">
            </div>
         </div>
      </div>
   `;


   productsGroup.innerHTML = content;
}
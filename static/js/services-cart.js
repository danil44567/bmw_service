let cart = JSON.parse(localStorage.getItem('cart')) || []

for (const id of cart) {
    updateCard(id, true)
}

function addCart(id) {
    if (cart.indexOf(id) === -1) {
        cart.push(id)
        updateCard(id, true)
        localStorage.setItem('cart', JSON.stringify(cart))
    }
}

function deleteCart(id) {
    const index = cart.indexOf(id)
    if (index !== -1) {
        cart.splice(index, 1)
        updateCard(id, false)
        localStorage.setItem('cart', JSON.stringify(cart))
    }
}

function updateCard(id, isAdd) {
    const cardBtn = document.getElementById(`add-cart-btn-${id}`);
    const cardBtnModal = document.getElementById(`add-cart-btn-modal-${id}`);
    if (!cardBtn || !cardBtnModal)
        return

    if (isAdd) {
        const selectedHtml = `<div class="d-flex align-items-center justify-content-center">
                            Выбрано
                            <span class="material-icons">
                                done
                            </span>
                        </div>`
        cardBtn.classList.replace('btn-outline-primary', 'btn-outline-success');
        cardBtnModal.classList.replace('btn-outline-primary', 'btn-outline-success');
        cardBtn.innerHTML = selectedHtml;
        cardBtnModal.innerHTML = selectedHtml;
    }
    else {
        const notSelectedHtml = `<div class="d-flex align-items-center justify-content-center">
                            Записаться
                            <span class="material-icons">
                                navigate_next
                            </span>
                        </div>`
        cardBtn.classList.replace('btn-outline-success', 'btn-outline-primary');
        cardBtnModal.classList.replace('btn-outline-success', 'btn-outline-primary');
        cardBtn.innerHTML = notSelectedHtml;
        cardBtnModal.innerHTML = notSelectedHtml;
    }
}
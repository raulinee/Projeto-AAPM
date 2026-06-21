/* ============================================================================
   HOME.JS - Lógica interativa do PDV
   ============================================================================ */

// Estado do Carrinho
let cart = [];

// Elementos do DOM
const productsGrid = document.getElementById('products-grid');
const searchInput = document.getElementById('search-input');
const categoryButtons = document.querySelectorAll('.category-btn');
const emptyCartState = document.getElementById('empty-cart-state');
const cartItemsList = document.getElementById('cart-items-list');
const cartTotal = document.getElementById('cart-total');
const checkoutBtn = document.getElementById('checkout-btn');

// Filtros Atuais
let currentSearch = "";
let currentCategory = "all";

/**
 * Renderiza o grid de produtos com base nos filtros atuais
 */
function renderProducts() {
    productsGrid.innerHTML = "";
    
    const filteredProducts = productsData.filter(product => {
        const matchesSearch = product.name.toLowerCase().includes(currentSearch.toLowerCase());
        const matchesCategory = currentCategory === "all" || product.category === currentCategory;
        return matchesSearch && matchesCategory;
    });

    if (filteredProducts.length === 0) {
        productsGrid.innerHTML = `
            <div style="grid-column: 1/-1; text-align: center; color: var(--text-muted); padding: 40px;">
                Nenhum produto encontrado.
            </div>
        `;
        return;
    }

    filteredProducts.forEach(product => {
        const card = document.createElement('div');
        card.className = 'product-card';
        card.onclick = () => addToCart(product.id);
        
        let imagemHtml = `
            <div class="product-image-placeholder">
                <i data-lucide="image"></i>
            </div>
        `;
        
        // Usa tag img apenas se não for o placeholder padrão do backend.
        if (product.imagem && product.imagem !== "None" && product.imagem !== "" && !product.imagem.includes("produto-placeholder.png")) {
            imagemHtml = `
            <img src="${product.imagem}" alt="${product.name}" 
                 style="width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 8px;"
                 onerror="this.outerHTML='<div class=\\'product-image-placeholder\\'><i data-lucide=\\'image\\'></i></div>'; setTimeout(() => lucide.createIcons(), 10);">
            `;
        }

        card.innerHTML = `
            ${imagemHtml}
            <div class="product-info">
                <span class="product-name" title="${product.name}">${product.name}</span>
                <span class="product-category">${product.category}</span>
            </div>
            <div class="product-footer">
                <span class="product-price">R$ ${product.price.toFixed(2).replace('.', ',')}</span>
                <button class="add-to-cart-btn" onclick="event.stopPropagation(); addToCart(${product.id})">
                    <i data-lucide="shopping-cart"></i>
                </button>
            </div>
        `;
        
        productsGrid.appendChild(card);
    });

    // Recriar ícones do Lucide
    lucide.createIcons();
}

/**
 * Adiciona um produto ao carrinho
 * @param {number} productId - ID do produto
 */
function addToCart(productId) {
    const product = productsData.find(p => p.id === productId);
    if (!product) return;

    const existingItem = cart.find(item => item.product.id === productId);

    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            product: product,
            quantity: 1
        });
    }

    updateCartUI();
}

/**
 * Altera a quantidade de um item no carrinho
 * @param {number} productId - ID do produto
 * @param {number} delta - Incremento/Decremento na quantidade
 */
function changeQuantity(productId, delta) {
    const item = cart.find(item => item.product.id === productId);
    if (!item) return;

    item.quantity += delta;

    if (item.quantity <= 0) {
        cart = cart.filter(item => item.product.id !== productId);
    }

    updateCartUI();
}

/**
 * Remove um item do carrinho
 * @param {number} productId - ID do produto
 */
function removeFromCart(productId) {
    cart = cart.filter(item => item.product.id !== productId);
    updateCartUI();
}

/**
 * Atualiza a interface do carrinho (lista de itens e total)
 */
function updateCartUI() {
    if (cart.length === 0) {
        emptyCartState.style.display = 'flex';
        cartItemsList.style.display = 'none';
        cartTotal.textContent = "R$ 0,00";
        
        checkoutBtn.disabled = true;
        checkoutBtn.classList.remove('active');
    } else {
        emptyCartState.style.display = 'none';
        cartItemsList.style.display = 'flex';
        
        cartItemsList.innerHTML = "";
        let total = 0;

        cart.forEach(item => {
            total += item.product.price * item.quantity;
            
            const li = document.createElement('li');
            li.className = 'cart-item';
            
            li.innerHTML = `
                <div class="cart-item-details">
                    <span class="cart-item-name">${item.product.name}</span>
                    <span class="cart-item-price">R$ ${(item.product.price * item.quantity).toFixed(2).replace('.', ',')}</span>
                </div>
                <div class="cart-item-actions">
                    <div class="quantity-control">
                        <button class="qty-btn" onclick="changeQuantity(${item.product.id}, -1)">
                            <i data-lucide="minus" style="width:12px;height:12px;"></i>
                        </button>
                        <span class="qty-val">${item.quantity}</span>
                        <button class="qty-btn" onclick="changeQuantity(${item.product.id}, 1)">
                            <i data-lucide="plus" style="width:12px;height:12px;"></i>
                        </button>
                    </div>
                    <button class="remove-item-btn" onclick="removeFromCart(${item.product.id})">
                        <i data-lucide="trash-2" style="width:14px;height:14px;"></i>
                    </button>
                </div>
            `;
            
            cartItemsList.appendChild(li);
        });

        cartTotal.textContent = `R$ ${total.toFixed(2).replace('.', ',')}`;
        
        checkoutBtn.disabled = false;
        checkoutBtn.classList.add('active');
    }

    lucide.createIcons();
}

/**
 * Event Listeners e inicialização
 */

// Evento de busca instantânea (ao digitar)
searchInput.addEventListener('input', (e) => {
    currentSearch = e.target.value;
    renderProducts();
});

// Mantemos o botão caso o usuário queira clicar
const searchBtn = document.getElementById('search-btn');
if (searchBtn) {
    searchBtn.addEventListener('click', () => {
        currentSearch = searchInput.value;
        renderProducts();
    });
}

// Evento de filtro de categoria
categoryButtons.forEach(button => {
    button.addEventListener('click', () => {
        categoryButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
        
        currentCategory = button.getAttribute('data-category');
        renderProducts();
    });
});

// Inicialização quando o DOM estiver pronto
document.addEventListener('DOMContentLoaded', () => {
    lucide.createIcons();
    renderProducts();
});

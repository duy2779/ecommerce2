const profileHeaderMenu = document.getElementById('header-profile')
const profileSubmenu = document.getElementById('profile-actions-dropdown')

profileHeaderMenu.addEventListener('click', () => {
    profileSubmenu.classList.toggle('show-profile-actions-dropdown')
})
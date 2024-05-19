let theme = false

const btnChangeTheme = document.querySelector('.btn_change_theme');
const body = document.querySelector('body');

btnChangeTheme.addEventListener('click', changeTheme);

function changeTheme() {
	if (theme == false) {
		btnChangeTheme.setAttribute('src', '/static/Core/img/moon.svg')
		body.setAttribute('data-bs-theme', 'light')
		theme = true
	} else {
		btnChangeTheme.setAttribute('src', '/static/Core/img/sun.svg')
		body.setAttribute('data-bs-theme', 'dark')
		theme = false
	}
	localStorage.setItem('theme', theme)
}

const loadedTheme = localStorage.setItem('theme')

if ( loadedTheme === 'true' ) (
	btnChangeTheme.setAttribute('src', '/static/Core/img/sun.svg')
	bod.setAttribute('data-bs-theme', 'light')
	theme = true
)

function copyToClipboard(text) {
	navigator.clipboard.writeText(text).then(() => {
		alert('Link copied to clipboard');
	}).catch(() => {
		console.log('Clipboard not available');
	});
}

function filterResources(term) {
	const cards = document.querySelectorAll('.resource-card');
	const q = term.toLowerCase();
	cards.forEach(card => {
		const title = card.querySelector('.resource-title')?.textContent.toLowerCase() || '';
		const desc = card.querySelector('.resource-description')?.textContent.toLowerCase() || '';
		const match = title.includes(q) || desc.includes(q);
		card.style.display = match ? '' : 'none';
	});
}

document.addEventListener('DOMContentLoaded', () => {
	const searchInput = document.getElementById('resourceSearch');
	if (searchInput) {
		searchInput.addEventListener('input', (e) => filterResources(e.target.value));
	}
});
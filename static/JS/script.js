const btnCopy = document.getElementById('copy');
const userData = document.getElementById('user-data');

if (btnCopy) {
  btnCopy.addEventListener('click', () => {
    navigator.clipboard.writeText(userData.innerText);
  });
}

// const form = document.querySelector('form');

// form.addEventListener('submit', (e) => {
//   e.preventDefault();
//   const username = form.querySelector('.form__input').value;
//   console.log(username);

//   fetch(form.action, {
//     method: form.method,
//     body: new FormData(form),
//     headers: {
//       'X-Requested-With': 'XMLHttpRequest',
//     },
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       // Handle the response from the server
//       console.log(data);
//       // Update the page as needed
//     });
// });

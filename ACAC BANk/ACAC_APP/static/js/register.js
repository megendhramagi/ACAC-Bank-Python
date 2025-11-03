document.getElementById('registerForm').addEventListener('submit', function (e) {
    e.preventDefault();
  
    const name = document.getElementById('name').value.trim();
    const age = parseInt(document.getElementById('age').value.trim(), 10);
    const phone = document.getElementById('phone').value.trim();
    const deposit = document.getElementById('deposit').value.trim();
    const errorMsg = document.getElementById('errorMsg');
  
    const nameValid = /^[a-zA-Z\s]+$/.test(name);
    const ageValid = !isNaN(age) && age > 0 && age < 150;
    const phoneValid = /^\d{10}$/.test(phone);
    const depositValid = /^\d+$/.test(deposit);
  
    if (!nameValid) {
      errorMsg.textContent = "Name must contain only letters and spaces.";
      return;
    }
  
    if (!ageValid) {
      errorMsg.textContent = "Age must be a number less than 150.";
      return;
    }
  
    if (!phoneValid) {
      errorMsg.textContent = "Phone number must be exactly 10 digits.";
      return;
    }
  
    if (!depositValid) {
      errorMsg.textContent = "Initial Deposit must be a valid number.";
      return;
    }
  
    errorMsg.textContent = "";
    alert("Registration successful!");
    // You can proceed with form submission here
  });
  
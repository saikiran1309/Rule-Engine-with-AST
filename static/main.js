// Create-Rule-form
document.getElementById('create-rule-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const ruleName = document.getElementById('ruleName').value.trim();
    const ruleString = document.getElementById('ruleString').value.trim();
    if (!ruleName || !ruleString) {
        alert("Please fill in both the rule name and rule string.");
        return;
    }
    const requestBody = { rule_name: ruleName, rule_string: ruleString };
    console.log('Request Body:', JSON.stringify(requestBody));
    try {
        const response = await fetch('/api/rules/create_rule', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestBody),
        });
        const result = await response.json();
        if (response.ok) {
            let treeHTML = generateTreeHTML(result.formatted_tree);
            treeHTML += `<br><p>Rule Name: ${result.ruleName}</p>`;
            document.getElementById('create-rule-result').innerHTML = result.formatted_tree.replace(/\n/g, '<br>');
            document.getElementById('create-rule-result').innerHTML += `<br><p>Rule Name: ${result.ruleName}</p>`;
        } else {
            document.getElementById('create-rule-result').textContent = result.detail || "Error creating rule.";
        }
    } catch (error) {
        console.error('Error creating rule:', error);
        document.getElementById('create-rule-result').textContent = "Error creating rule.";
    }
});


// Combine-Rules-form
document.getElementById('combine-rules-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const op = document.getElementById('operator1').value; // Ensure the correct ID is used
    const rules = Array.from(document.querySelectorAll('input[id^="combine-rule"]')).map(input => input.value.trim());
    try {
        const response = await fetch('/api/rules/combine_rules', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ rules, op }),
        });
        console.log('Response status:', response.status);
        const result = await response.json();
        console.log('Result from server:', result);
        if (response.ok) {
            // Generate the tree HTML from result.formatted_tree
            document.getElementById('combine-rules-result').innerHTML = result.formatted_tree.replace(/\n/g, '<br>');
            document.getElementById('combine-rules-result').innerHTML += `<br><br><p>Rule Name: ${result.ruleName}</p>`;
        } else {
            throw new Error(result.detail || 'Error combining rules.');
        }
    } catch (error) {
        console.error('Error combining rules:', error);
        document.getElementById('combine-rules-result').textContent = "Error combining rules.";
    }
});

// Add-rule
document.getElementById('add-rule').addEventListener('click', function() {
    const ruleInputContainer = document.createElement('div');
    ruleInputContainer.classList.add('rule-container');
    const ruleCount = document.querySelectorAll('input[id^="combine-rule"]').length + 1;
    ruleInputContainer.innerHTML = `
        <label for="combine-rule${ruleCount}">Rule ${ruleCount}:</label>
        <input type="text" id="combine-rule${ruleCount}" name="rule${ruleCount}" required>
    `;
    document.getElementById('rules-inputs').appendChild(ruleInputContainer); // Add new input container
    this.remove(); // Remove the button
});


// Evaluate-Rule-form
document.getElementById('evaluate-rule-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the default form submission behavior
    const ast = document.getElementById('evaluate-ast').value.trim(); // Get Rule AST input
    const dataInput = document.getElementById('evaluate-data').value.trim(); // Get Data JSON input
    if (!ast || !dataInput) {
        alert("Please fill in both the Rule AST and Data fields.");
        return;
    }
    let data;
    try {
        data = JSON.parse(dataInput); // Parse Data JSON
    } catch (error) {
        alert("Invalid data format. Enter valid JSON.");
        return;
    }
    try {
        const response = await fetch('/api/rules/evaluate_rule', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ ast, data }), // Send AST and Data in the request body
        });
        if (response.ok) {
            const result = await response.json();
            document.getElementById('evaluate-rule-result').textContent = JSON.stringify(result, null, 2); // Display result
        } else {
            document.getElementById('evaluate-rule-result').textContent = `Error: ${response.statusText}`; // Handle error
        }
    } catch (error) {
        console.error('Error evaluating rule:', error);
        document.getElementById('evaluate-rule-result').textContent = "Error evaluating rule."; // Display error message
    }
});


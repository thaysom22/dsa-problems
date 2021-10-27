import React, { useState } from 'react';
import ReactDOM from 'react-dom';

// define style object
const style = {
  table: {
    borderCollapse: 'collapse'
  },
  tableCell: {
    border: '1px solid gray',
    margin: 0,
    padding: '5px 10px',
    width: 'max-content',
    minWidth: '150px'
  },
  form: {
    container: {
      padding: '20px',
      border: '1px solid #F0F8FF',
      borderRadius: '15px',
      width: 'max-content',
      marginBottom: '40px'
    },
    inputs: {
      marginBottom: '5px'
    },
    submitBtn: {
      marginTop: '10px',
      padding: '10px 15px',
      border:'none',
      backgroundColor: 'lightseagreen',
      fontSize: '14px',
      borderRadius: '5px'
    }
  }
}


function PhoneBookForm({ addEntry }) {
  // define initial entry
  const initEntry = {
    id: null,
    userFirstname: "Coder",
    userLastname: "Byte",
    userPhone: "8885559999",
  };

  // store entry state at form component level
  const [entryState, setEntryState] = useState(initEntry);

  // define handler to update entry state whenever any input changes
  const handleEntryChange = (e) => {
    setEntryState({
      ...entryState,
      [e.target.name]: e.target.value,
    });
  }

  // define handler to add entry to phonebook state and reset entry state when form is submitted
  const handleEntrySubmit = (e) => {
    e.preventDefault();
    if (!entryState.userFirstname || !entryState.userLastname || !entryState.userPhone) return;
    addEntry(entryState);
    setEntryState(initEntry);
  }

  // render form with submit handler and inputs for each entry field
  // each input takes respective property value from current entry state and updates entry state via handler on change
  return (
    <form 
      onSubmit={handleEntrySubmit}
      style={style.form.container}
    >
      <label>First name:</label>
      <br />
      <input 
        style={style.form.inputs}
        className='userFirstname'
        name='userFirstname' 
        type='text'
        value={ entryState.userFirstname }
        onChange={handleEntryChange}
      />
      <br/>
      <label>Last name:</label>
      <br />
      <input 
        style={style.form.inputs}
        className='userLastname'
        name='userLastname' 
        type='text'
        value={ entryState.userLastname }
        onChange={handleEntryChange} 
      />
      <br />
      <label>Phone:</label>
      <br />
      <input
        style={style.form.inputs}
        className='userPhone' 
        name='userPhone' 
        type='text'
        value={ entryState.userPhone }
        onChange={handleEntryChange}
      />
      <br/>
      <input 
        style={style.form.submitBtn} 
        className='submitButton'
        type='submit' 
        value='Add User' 
      />
    </form>
  )
}


function InformationTable({ phoneBookState }) {
  // generate phonebook sorted by last name
  const sortedPhoneBook = phoneBookState.sort((a,b) => a.userLastname.localeCompare(b.userLastname));
  
  // define element to represent rows in table for all phonebook entries, including new entry
  const display =
    sortedPhoneBook.length > 0 ? (
      sortedPhoneBook.map((entry, i) => (
        <tr key={i}>
          <td style={style.tableCell}>{entry.userFirstname}</td>
          <td style={style.tableCell}>{entry.userLastname}</td>
          <td style={style.tableCell}>{entry.userPhone}</td>
        </tr>
      ))
    ) : (
      <tr>
        <td colSpan={3}>&nbsp;</td>
      </tr>
    );

  // render table with all sorted phonebook entries
  return (
    <table style={style.table} className='informationTable'>
      <thead> 
        <tr>
          <th style={style.tableCell}>First name</th>
          <th style={style.tableCell}>Last name</th>
          <th style={style.tableCell}>Phone</th>
        </tr>
      </thead>
      <tbody>{display}</tbody>
    </table>
  );
}

function Application(props) {
  // store phonebook state at application level
  const [phoneBookState, setPhoneBookState] = useState([]);

  // function to add new entry to phonebook state
  const addEntry = entry => {
    entry.id = phoneBookState.length + 1;
    setPhoneBookState([...phoneBookState, entry]);
  }

  // pass function to add new entry to phone book to PhoneBookForm
  // pass phonebook state to InformationTable
  return (
    <section>
      <PhoneBookForm 
        addEntry={addEntry}
      />
      <InformationTable 
        phoneBookState={phoneBookState}
      />
    </section>
  );
}

ReactDOM.render(
  <Application />,
  document.getElementById('root')
);
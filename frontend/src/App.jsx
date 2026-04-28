import { useEffect, useState } from "react";
import { getItems, createItem, deleteItem, getRecommendation } from "./api";
import "./App.css";

function App() {
  const [items, setItems] = useState([]);
  const [form, setForm] = useState({
    name: "",
    category: "",
    quantity: "",
    price: "",
    supplier: ""
  });
  const [recommendation, setRecommendation] = useState("");

  const loadItems = async () => {
    const response = await getItems();
    setItems(response.data);
  };

  useEffect(() => {
    loadItems();
  }, []);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    await createItem({
      name: form.name,
      category: form.category,
      quantity: Number(form.quantity),
      price: Number(form.price),
      supplier: form.supplier
    });

    setForm({
      name: "",
      category: "",
      quantity: "",
      price: "",
      supplier: ""
    });

    loadItems();
  };

  const handleDelete = async (id) => {
    await deleteItem(id);
    loadItems();
  };

  const handleRecommendation = async (id) => {
    const response = await getRecommendation(id);
    setRecommendation(response.data.recommendation);
  };

  return (
    <div className="container">
      <h1>AI Inventory Manager</h1>

      <form onSubmit={handleSubmit}>
        <input name="name" placeholder="Item Name" value={form.name} onChange={handleChange} required />
        <input name="category" placeholder="Category" value={form.category} onChange={handleChange} required />
        <input name="quantity" placeholder="Quantity" value={form.quantity} onChange={handleChange} required />
        <input name="price" placeholder="Price" value={form.price} onChange={handleChange} required />
        <input name="supplier" placeholder="Supplier" value={form.supplier} onChange={handleChange} required />
        <button type="submit">Add Item</button>
      </form>

      {recommendation && <p className="recommendation">{recommendation}</p>}

      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Category</th>
            <th>Qty</th>
            <th>Price</th>
            <th>Supplier</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          {items.map((item) => (
            <tr key={item.id}>
              <td>{item.name}</td>
              <td>{item.category}</td>
              <td>{item.quantity}</td>
              <td>${item.price}</td>
              <td>{item.supplier}</td>
              <td>
                <button onClick={() => handleRecommendation(item.id)}>AI Suggest</button>
                <button onClick={() => handleDelete(item.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
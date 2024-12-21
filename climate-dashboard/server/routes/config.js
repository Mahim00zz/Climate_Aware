const express = require('express');
const { get } = require('@vercel/edge-config');

const router = express.Router();

router.get('/config', async (req, res) => {
  try {
    const value = await get('db_connection_string');  // Replace with your actual key
    res.status(200).json({ value });
  } catch (error) {
    console.error('Error fetching config:', error);
    res.status(500).json({ error: 'Error fetching config' });
  }
});

module.exports = router;

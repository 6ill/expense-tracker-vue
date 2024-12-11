<template>
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white shadow-lg rounded-lg p-8 max-w-md w-full">
      <h1 class="text-2xl font-bold text-center text-blue-700">Edit Transaction</h1>
      <!-- Tampilkan loading jika sedang memuat -->
      <div v-if="isLoading" class="text-center text-blue-600 my-4">
        Loading transaction data...
      </div>
      <form v-else class="mt-6 space-y-4" @submit.prevent="handleSubmit">
        <div>
          <label for="date" class="block text-sm font-medium text-gray-700">Date</label>
          <input
            type="date"
            id="date"
            v-model="date"
            class="w-full mt-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-600 focus:outline-none"
            required
          />
        </div>
        <div>
          <label for="amount" class="block text-sm font-medium text-gray-700">Amount</label>
          <input
            type="number"
            id="amount"
            v-model="amount"
            placeholder="Enter amount"
            class="w-full mt-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-600 focus:outline-none"
            required
          />
        </div>
        <div>
          <label for="category" class="block text-sm font-medium text-gray-700">Category</label>
          <select
            id="category"
            v-model="category"
            class="w-full mt-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-600 focus:outline-none"
            required
          >
            <option value="food">Food</option>
            <option value="lifestyle">Lifestyle</option>
            <option value="travel">Travel</option>
            <option value="entertainment">Entertainment</option>
            <option value="other">Other</option>
          </select>
        </div>
        <div>
          <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
          <textarea
            id="description"
            v-model="description"
            placeholder="Enter description"
            class="w-full mt-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-600 focus:outline-none"
            required
          ></textarea>
        </div>
        <button
          type="submit"
          class="w-full bg-blue-600 text-white font-bold py-2 px-4 rounded-lg shadow hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600"
        >
          Save Changes
        </button>
      </form>
    </div>
  </div>
</template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  import apiClient from '../../apiClient';

  export default {
    setup() {
      const router = useRouter();
      const route = useRoute();
      const category = ref('');
      const amount = ref('');
      const date = ref('');
      const description = ref('');
      const isLoading = ref(false); // Tambahkan loading state

      // Fungsi untuk mengambil data transaksi
      const fetchTransaction = async () => {
        isLoading.value = true; // Tampilkan indikator loading
        try {
          const response = await apiClient.get(`/transactions/${route.params.transactionId}`);
          if (response.data.status === 'success') {
            const transaction = response.data.transaction;
            category.value = transaction.category;
            amount.value = transaction.amount;
            
            const dateTimeObject = new Date(transaction.date);
            const pad = (num) => String(num).padStart(2, '0');
            const year = dateTimeObject.getFullYear();
            const month = pad(dateTimeObject.getMonth() + 1);
            const day = pad(dateTimeObject.getDate());
            const dateString = `${year}-${month}-${day}`;
            
            date.value = dateString;
            description.value = transaction.desc;
          } else {
            alert('Failed to fetch transaction. Please try again.');
          }
        } catch (error) {
          console.error('Failed to fetch transaction:', error);
          alert('Failed to fetch transaction. Please try again.');
        } finally {
          isLoading.value = false; // Sembunyikan indikator loading
        }
      };

      // Fungsi untuk memperbarui transaksi
      const handleSubmit = async () => {
        if (!category.value || !amount.value || !date.value || !description.value) {
          alert('All fields are required!');
          return;
        }

        isLoading.value = true; // Tampilkan indikator loading
        try {
          const response = await apiClient.put(`/transactions/${route.params.transactionId}`, {
            category: category.value,
            amount: amount.value,
            date: date.value,
            description: description.value,
          });
          if (response.data.status === 'success') {
            alert('Transaction updated successfully!');
            router.push({ name: 'MainWorkspace' });
          } else {
            alert(response.data.message || 'Failed to update transaction. Please try again.');
          }
        } catch (error) {
          console.error('Failed to update transaction:', error);
          alert('Failed to update transaction. Please try again.');
        } finally {
          isLoading.value = false; // Sembunyikan indikator loading
        }
      };

      onMounted(() => {
        fetchTransaction(); // Ambil data transaksi saat halaman dimuat
      });

      return {
        category,
        amount,
        date,
        description,
        handleSubmit,
        isLoading, // Untuk indikator loading
      };
    },
  };
  </script>
  
  <style scoped>
  body {
    font-family: 'Arial', sans-serif;
    background-color: #f0f4f8;
    margin: 0;
    padding: 0;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  </style>
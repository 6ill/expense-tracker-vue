<template>
  <div class="min-h-screen bg-gray-50 p-4">
    <header class="flex justify-between items-center mb-4">
      <div class="flex items-center space-x-4">
        <div>
          <label for="start-date" class="block text-sm font-medium text-gray-700">Start Date:</label>
          <input type="date" id="start-date" v-model="startDate" @change="filterTransactions" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm" />
        </div>
        <div>
          <label for="end-date" class="block text-sm font-medium text-gray-700">End Date:</label>
          <input type="date" id="end-date" v-model="endDate" @change="filterTransactions" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm" />
        </div>
      </div>
      <div class="flex items-center space-x-4">
        <div v-for="(column, index) in columns" :key="index" class="flex items-center space-x-2">
          <input type="checkbox" v-model="column.visible" class="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500" />
          <label class="text-sm font-medium text-gray-700">{{ column.name }}</label>
        </div>
        <button @click="logout" class="bg-red-500 text-white px-4 py-2 rounded-md shadow hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">Logout</button>
      </div>
    </header>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
      <div 
        v-for="(column, index) in visibleColumns" 
        :key="index"
        :class="column.total > column.limit ? 'bg-red-100' : 'bg-white'"
        class="p-4 rounded-lg shadow">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-lg font-medium text-gray-900">{{ column.name }}</h3>
          <div class="flex space-x-2">
            <button @click="addTransaction(column.name)" class="bg-blue-500 text-white px-2 py-1 rounded-md shadow hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">+</button>
            <button @click="editLimit(index)" class="bg-yellow-500 text-white px-2 py-1 rounded-md shadow hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-yellow-500">Edit Limit</button>
          </div>
        </div>
        <div class="space-y-2">
          <div v-for="transaction in filteredTransactions[index]" :key="transaction.id" class="bg-gray-100 p-2 rounded-md shadow cursor-pointer" @dblclick="editTransaction(transaction, index)">
            <p class="text-sm font-medium text-gray-700">{{ transaction.amount }}</p>
            <p class="text-sm text-gray-500">{{ transaction.date }}</p>
            <p class="text-sm text-gray-600">{{ transaction.desc }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, reactive, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import apiClient from '../../apiClient';

export default {
  setup() {
    const router = useRouter();
    const startDate = ref('');
    const endDate = ref('');
    const columns = reactive([
      { name: 'food', transactions: [], visible: true, limit: 0, total: 0 },
      { name: 'lifestyle', transactions: [], visible: true, limit: 0, total: 0 },
      { name: 'travel', transactions: [], visible: true, limit: 0, total: 0 },
      { name: 'entertainment', transactions: [], visible: true, limit: 0, total: 0 },
      { name: 'other', transactions: [], visible: true, limit: 0, total: 0 },
    ]);

    const visibleColumns = computed(() => {
      return columns.filter(column => column.visible);
    });

    const filteredTransactions = computed(() => {
      return columns.map(column => {
        return column.transactions.filter(transaction => {
          const transactionDate = new Date(transaction.date);
          const start = new Date(startDate.value);
          const end = new Date(endDate.value);
          return (!startDate.value || transactionDate >= start) && (!endDate.value || transactionDate <= end);
        });
      });
    });

    const fetchLimits = async () => {
      try {
        const response = await apiClient.get('/limits/');
        if (response.data.status === 'success') {
          const limits = response.data.limits;
          columns.forEach(column => {
            column.limit = limits[column.name.toLowerCase()];
          });
        }
      } catch (error) {
        console.error('Failed to fetch limits:', error);
      }
    };

    const fetchTransactions = async () => {
      try {
        for (const column of columns) {
          const response = await apiClient.get(`/transactions/category/${column.name.toLowerCase()}`);
          if (response.data.status === 'success') {
            column.transactions = response.data.transactions;
            updateTotal(column);
          }
        }
      } catch (error) {
        console.error('Failed to fetch transactions:', error);
      }
    };

    const addTransaction = (category) => {
      router.push({ name: 'AddTransaction', params: { category } });
    };

    const editTransaction = (transaction, index) => {
      const action = confirm(`
        Pilih aksi untuk transaksi:
        - Klik "OK" untuk mengedit.
        - Klik "Cancel" untuk menghapus.
      `);

      if (action) {
        // Isi data transaksi ke form edit
        router.push({
          name: 'EditTransaction',
          params: {
            transactionId: transaction.id,
            column: index,
            data: {
              amount: transaction.amount,
              date: transaction.date,
              description: transaction.description,
            },
          },
        });
      } else {
        const deleteAction = confirm('Anda yakin ingin menghapus transaksi ini?');
        if (deleteAction) {
          // Hapus transaksi dari kolom
          columns[index].transactions = columns[index].transactions.filter(
            (t) => t.id !== transaction.id
          );
          updateTotal(columns[index]);
        } else {
          console.log('Aksi dibatalkan');
        }
      }
    };

    const editLimit = (index) => {
      const newLimit = prompt('Enter new limit:', columns[index].limit);
      if (newLimit !== null) {
        columns[index].limit = parseFloat(newLimit);
        updateLimit(columns[index].name.toLowerCase(), newLimit);
      }
    };

    const updateLimit = async (type, budget) => {
      try {
        await apiClient.put('/limits/', { type, budget });
      } catch (error) {
        console.error('Failed to update limit:', error);
      }
    };

    const toggleColumn = (index) => {
      columns[index].visible = !columns[index].visible;
    };

    const filterTransactions = () => {
      // This will automatically update the filteredTransactions computed property
    };

    const updateTotal = (column) => {
      column.total = column.transactions.reduce((sum, transaction) => sum + parseFloat(transaction.amount), 0);
      console.log(`Updated total for ${column.name}:`, column.total, 'Limit:', column.limit);
    };

    const logout = async () => {
      try {
        await apiClient.post('/users/logout');
        router.push({ name: 'Login' });
      } catch (error) {
        console.error('Logout error:', error);
      }
    };

    onMounted(() => {
      fetchLimits();
      fetchTransactions();
    });

    return {
      startDate,
      endDate,
      columns,
      visibleColumns,
      filteredTransactions,
      addTransaction,
      editTransaction,
      editLimit,
      toggleColumn,
      filterTransactions,
      logout,
    };
  },
};
</script>

<style scoped>
.main-workspace {
  padding: 20px;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
.date-range {
  display: flex;
  align-items: center;
}
.date-range label {
  margin-right: 10px;
}
.column-toggles {
  display: flex;
  align-items: center;
}
.column-toggles label {
  margin-right: 10px;
}
.transaction-table {
  display: flex;
  justify-content: space-between;
}
.column-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
.transactions {
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
}
.transaction-card {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  cursor: pointer;
}
.over-limit {
  background-color: #ffcccc;
}
</style>
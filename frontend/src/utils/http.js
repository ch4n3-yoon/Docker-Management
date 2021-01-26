import axios from 'axios';


const http = axios.create({
  baseURL: 'http://ch4n3.kr:2300/api/',
  headers: localStorage.getItem('token') && {
    'Authorization': `JWT ${localStorage.getItem('token')}`
  },
});


export default http;

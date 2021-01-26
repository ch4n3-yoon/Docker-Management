import React, {useState} from 'react';
import {Container, Header, Form, Segment} from 'semantic-ui-react';
import 'semantic-ui-css/semantic.min.css';
import http from '../utils/http';


const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(false);

  const handleUsername = (event) => {
    setUsername(event.target.value);
  };

  const handlePassword = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = () => {
    http.post('/user/token', {
      username: username,
      password: password,
    })
      .then((resp) => {
        console.log('[ DEBUG ] resp :', resp);
        localStorage.setItem('token', resp.data.token);
        http.defaults.headers.common['Authorization'] = `JWT ${resp.data.token}`;
      })
      .catch((error) => {
        setError(true);
      });
  }

  if (error) {
    return (
      <div>
        error !
      </div>
    )
  }

  return (
    <Container>
      <Segment raised>
        <Header as="h2" color="purple">
          Login
        </Header>
        <Form onSubmit={handleSubmit}>
          <Form.Field
            label='username'
            type='text'
            placeholder='Username'
            onChange={handleUsername}
          />
          <Form.Field
            label='password'
            type='password'
            placeholder='Password'
            onChange={handlePassword}
          />
        </Form>
      </Segment>
    </Container>
  );
};

export default Login;

export const API_END_PONT = "http://127.0.0.1:8000";

export const api = async (route, {
    method,
    body,
    ...customConfig
    }) => {
    try {
        const headers = {
            'Content-Type': 'application/json',
        };

        // const token = LS.get(LOCAL_STORAGE_KEYS.AUTH_TOKEN);
        // if (token) {
        //     headers['Authorization'] = 'Bearer ' + token;
        // }

        const config = {
            method: method ? method : (body ? 'POST' : 'GET'),
            ...customConfig,
            headers: {
                ...headers,
                ...customConfig.headers,
            },
        };

        if (body) {
            if (body.formData) {
                config.body = body.formData;
                delete config.headers['Content-Type'];
            } else {
                config.body = JSON.stringify(body);
            }
        }

        const response = await fetch(`${API_END_PONT}${route}`, {
            ...config,
        });
        let jsonResponse;
        const contentType = await response.headers.get("content-type");
        
        if (contentType && contentType.indexOf("application/json") !== -1) {
            jsonResponse = await response.json();
        } else {
            return await response.blob()
        }

        if (response.ok) {
            return jsonResponse;
        } else {
            if (response.status === 401) {
                AuthState.logout();
            }
            const error = new Error(response.statusText || response.status);
            error.code = response.status;
            error.response = response;
            error.message = jsonResponse.message || jsonResponse.detail;
            throw error;
        }

    } catch (error) {
        console.error(error.message);
        return Promise.reject(error);
    }
}
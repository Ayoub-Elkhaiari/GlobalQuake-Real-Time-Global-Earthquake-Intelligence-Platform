import {useEffect} from 'react';import {API} from '../api/earthquakeApi';
export function useEarthquakeWebSocket(onEvent){useEffect(()=>{const ws=new WebSocket(API.replace(/^http/,'ws')+'/ws/earthquakes');ws.onmessage=e=>onEvent(JSON.parse(e.data).event);return()=>ws.close()},[onEvent])}

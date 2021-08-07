import React from "react";
import Square from "./Square";
import { canMoveKnight, moveKnight } from "./Game";
import { ItemTypes } from "./ItemTypes";
import { useDrop } from "react-dnd";
import { Overlay, OverlayType } from "./Overlay";

function BoardSquare({ x, y, children }) {
	const black = (x + y) % 2 === 1;
	const [{ isOver, canDrop }, drop] = useDrop(
		() => ({
			accept: ItemTypes.KNIGHT,
			drop: () => moveKnight(x, y),
			canDrop: () => canMoveKnight(x, y),
			collect: (monitor) => ({
				isOver: !!monitor.isOver(),
				canDrop: !!monitor.canDrop(),
			}),
		}),
		[x, y]
	);

	return (
		<div
			ref={drop}
			style={{
				position: "relative",
				width: "100%",
				height: "100%",
			}}
		>
			<Square black={black}>{children}</Square>
			{isOver && !canDrop && <Overlay type={OverlayType.IllegalMoveHover}/>}
			{!isOver && canDrop && <Overlay type={OverlayType.PossibleMove}/>}
			{isOver && canDrop && <Overlay type={OverlayType.LegalMoveHover}/>}
			{/* {isOver && !canDrop && <Overlay color="red" />}
			{!isOver && canDrop && <Overlay color="yellow" />}
			{isOver && canDrop && <Overlay color="green" />} */}
		</div>
	);
}

export default BoardSquare;

// import React from "react";
// import { Square } from "./Square";
// import { canMoveKnight, moveKnight } from "./Game";
// import { ItemTypes } from "./ItemTypes";
// import { useDrop } from "react-dnd";
// import { Overlay, OverlayType } from './Overlay';

// export default function BoardSquare({ x, y, children }) {
// 	const [{ isOver, canDrop }, drop] = useDrop(
// 		() => ({
// 			accept: ItemTypes.KNIGHT,
// 			drop: () => moveKnight(x, y),
// 			collect: (monitor) => ({
// 				isOver: !!monitor.isOver(),
// 				canDrop: !!monitor.canDrop(),
// 			}),
// 		}),
// 		[x, y]
// 	);

// 	const black = (x + y) % 2 === 1;
//   return (
//     <div
//       ref={drop}
//       style={{
//         position: 'relative',
//         width: '100%',
//         height: '100%'
//       }}
//     >
//       <Square black={black}>{children}</Square>
//       {isOver && !canDrop && <Overlay color="red" />}
//       {!isOver && canDrop && <Overlay color="yellow" />}
//       {isOver && canDrop && <Overlay color="green" />}
//     </div>
//   )

// 	// return <Square black={black}>{children}</Square>;
// 	// return (
// 	// 	<div
// 	// 		ref={drop}
// 	// 		style={{
// 	// 			position: "relative",
// 	// 			width: "100%",
// 	// 			height: "100%",
// 	// 		}}
// 	// 	>
// 	// 		<Square black={black}>{children}</Square>
// 	// 		{isOver && !canDrop && <Overlay color="red" />}
// 	// 		{!isOver && canDrop && <Overlay color="yellow" />}
// 	// 		{isOver && canDrop && <Overlay color="green" />}
// 	// 		{/* {isOver && (
//   //       <div
//   //         style={{
//   //           position: 'absolute',
//   //           top: 0,
//   //           left: 0,
//   //           height: '100%',
//   //           width: '100%',
//   //           zIndex: 1,
//   //           opacity: 0.5,
//   //           backgroundColor: 'yellow',
//   //         }}
//   //       />
//   //     )} */}
// 	// 	</div>
// 	// );
// }
